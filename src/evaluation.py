"""
Módulo para avaliação do modelo de machine learning.
"""

import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from joblib import load
import logging
import yaml

from model_first import preprocessar_dados

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

def carregar_modelo(caminho_modelo: str):
    """
    Carrega o modelo treinado de um arquivo.

    Args:
        caminho_modelo (str): Caminho para o arquivo do modelo.

    Returns:
        Pipeline: Modelo carregado.
    """
    logging.info(f"Carregando modelo do arquivo: {caminho_modelo}")
    return load(caminho_modelo)

def avaliar_modelo(modelo, X_teste, y_teste):
    """
    Avalia o modelo usando o dataset de teste.

    Args:
        modelo (Pipeline): Modelo treinado.
        X_teste (pd.DataFrame): Features do dataset de teste.
        y_teste (pd.Series): Variável alvo do dataset de teste.

    Returns:
        dict: Métricas de avaliação do modelo.
    """
    logging.info("Avaliando o modelo")
    y_pred = modelo.predict(X_teste)
    metrics = {
        "MAE": mean_absolute_error(y_teste, y_pred),
        "MSE": mean_squared_error(y_teste, y_pred),
        "R2": r2_score(y_teste, y_pred)
    }
    return metrics

if __name__ == "__main__":
    config = carregar_config("config/config.yaml")
    
    logging.basicConfig(filename=config['logging']['log_file'], level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    dados_teste = pd.read_csv("data/dataset_teste.csv")
    X_teste, y_teste, preprocessor = preprocessar_dados(dados_teste)
    modelo = carregar_modelo(config['model']['save_path'])
    metrics = avaliar_modelo(modelo, X_teste, y_teste)
    for metric, value in metrics.items():
        logging.info(f"{metric}: {value:.4f}")
