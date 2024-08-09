"""
Módulo para criação e treinamento do modelo de machine learning.
"""

import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from joblib import dump
import logging
import yaml

def carregar_config(config_path: str):
    """
    Carrega as configurações do arquivo YAML.

    Args:
        config_path (str): Caminho para o arquivo de configuração YAML.

    Returns:
        dict: Dicionário com as configurações carregadas.
    """
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def carregar_dados(nome_arquivo: str) -> pd.DataFrame:
    """
    Carrega o dataset de um arquivo CSV.

    Args:
        nome_arquivo (str): Nome do arquivo CSV.

    Returns:
        pd.DataFrame: DataFrame contendo o dataset carregado.
    """
    logging.info(f"Carregando dados do arquivo: {nome_arquivo}")
    return pd.read_csv(nome_arquivo)

def preprocessar_dados(dados: pd.DataFrame):
    """
    Pré-processa os dados do dataset.

    Args:
        dados (pd.DataFrame): DataFrame contendo o dataset.

    Returns:
        X (pd.DataFrame): Features do dataset pré-processadas.
        y (pd.Series): Variável alvo (preço).
        preprocessor: Pipeline de pré-processamento.
    """
    X = dados.drop("Preco", axis=1)
    y = dados["Preco"]
    
    features_categoricas = ["Material", "TipoVenda", "TipoBarco"]
    features_numericas = ["Comprimento", "Largura", "Peso"]

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), features_numericas),
            ('cat', OneHotEncoder(handle_unknown='ignore'), features_categoricas)
        ])

    return X, y, preprocessor

def treinar_modelo(X, y, preprocessor, save_path: str):
    """
    Treina o modelo de árvore de decisão utilizando GridSearchCV para otimização de hiperparâmetros.

    Args:
        X (pd.DataFrame): Features do dataset.
        y (pd.Series): Variável alvo (preço).
        preprocessor: Pipeline de pré-processamento.
        save_path (str): Caminho para salvar o modelo treinado.

    Returns:
        Pipeline: Modelo treinado.
    """
    logging.info("Treinando o modelo de árvore de decisão com GridSearchCV")

    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', DecisionTreeRegressor(random_state=42))
    ])

    param_grid = {
        'regressor__max_depth': [10, 15, 20],
        'regressor__min_samples_split': [5, 10, 20],
        'regressor__min_samples_leaf': [2, 5, 10]
    }

    grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
    grid_search.fit(X, y)
    
    melhor_modelo = grid_search.best_estimator_
    dump(melhor_modelo, save_path)
    logging.info(f"Melhor modelo treinado salvo em {save_path} com os parâmetros: {grid_search.best_params_}")
    return melhor_modelo

def obter_nomes_features(preprocessor, X):
    """
    Ajusta o pré-processador e obtém os nomes das features após o pré-processamento.

    Args:
        preprocessor (ColumnTransformer): Pipeline de pré-processamento.
        X (pd.DataFrame): DataFrame de features.

    Returns:
        list: Lista com os nomes das features.
    """
    # Ajusta o pré-processador com os dados de entrada
    preprocessor.fit(X)
    
    # Obtém os nomes das features categóricas
    cat_features = preprocessor.named_transformers_['cat'].get_feature_names_out(preprocessor.transformers[1][2])
    
    # Obtém os nomes das features numéricas
    num_features = preprocessor.transformers[0][2]
    
    # Combina ambas em uma lista
    feature_names = list(num_features) + list(cat_features)
    
    return feature_names

if __name__ == "__main__":
    config = carregar_config("config/config.yaml")
    
    logging.basicConfig(filename=config['logging']['log_file'], level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    dados_treino = carregar_dados("data/dataset_treino.csv")
    X_treino, y_treino, preprocessor = preprocessar_dados(dados_treino)
    
    # Ajuste o pré-processador e obtenha os nomes das features
    feature_names = obter_nomes_features(preprocessor, X_treino)
    
    modelo = treinar_modelo(X_treino, y_treino, preprocessor, config['model']['save_path'])
    logging.info(f"Nomes das features: {feature_names}")
