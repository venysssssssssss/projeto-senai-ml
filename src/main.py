"""
Script principal para execução do projeto.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_generation import gerar_dataset, salvar_dataset, carregar_config
from model_first import carregar_dados, preprocessar_dados, treinar_modelo, obter_nomes_features
from evaluation import carregar_modelo, avaliar_modelo
from model_visualization import plot_predictions, plot_residuals, plot_feature_importances
import logging

def main():
    # Carregar configurações
    config = carregar_config("config/config.yaml")
    
    # Configurar logging
    logging.basicConfig(filename=config['logging']['log_file'], level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Geração dos datasets
    logging.info("Gerando datasets de treino e teste")
    dataset_treino = gerar_dataset(config['data']['num_samples'])
    dataset_teste = gerar_dataset(int(config['data']['num_samples'] * config['data']['test_size']))
    salvar_dataset(dataset_treino, "data/dataset_treino.csv")
    salvar_dataset(dataset_teste, "data/dataset_teste.csv")

    # Treinamento do modelo
    logging.info("Treinando o modelo")
    dados_treino = carregar_dados("data/dataset_treino.csv")
    X_treino, y_treino, preprocessor = preprocessar_dados(dados_treino)
    feature_names = obter_nomes_features(preprocessor, X_treino)
    modelo = treinar_modelo(X_treino, y_treino, preprocessor, config['model']['save_path'])

    # Avaliação do modelo
    logging.info("Avaliando o modelo treinado")
    dados_teste = carregar_dados("data/dataset_teste.csv")
    X_teste, y_teste, preprocessor = preprocessar_dados(dados_teste)
    modelo = carregar_modelo(config['model']['save_path'])
    metrics = avaliar_modelo(modelo, X_teste, y_teste)
    
    logging.info("Métricas de Avaliação do Modelo:")
    for metric, value in metrics.items():
        logging.info(f"{metric}: {value:.4f}")
    
    # Visualização dos resultados
    y_pred = modelo.predict(X_teste)
    plot_predictions(y_teste, y_pred)
    plot_residuals(y_teste, y_pred)
    plot_feature_importances(modelo, feature_names)

if __name__ == "__main__":
    main()