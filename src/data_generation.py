"""
Módulo para geração dos datasets de treino e teste usando a biblioteca faker.
"""

import pandas as pd
from faker import Faker
import random
import yaml
import logging

fake = Faker()

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

def gerar_dataset(n_amostras: int) -> pd.DataFrame:
    """
    Gera um dataset falso com n_amostras amostras.

    Args:
        n_amostras (int): Número de amostras a serem geradas.

    Returns:
        pd.DataFrame: DataFrame contendo o dataset gerado.
    """
    materiais = ["Termoplástico", "Alumínio", "GRP", "PVC", "Plástico", "Madeira", 
                 "Aço", "Hypalon", "Fibra de Carbono", "Concreto Reforçado", "Borracha"]
    tipos_venda = ["barco novo em estoque", "barco usado", "barco novo encomendado", "modelo de exibição"]
    tipos_barco = ["Barco console central", "Barco de pesca", "Catamarã", "Barco esportivo", "Lancha", 
                   "Pilothouse", "Barco de cabine", "Barco de deck", "Barco de pontão", "Clássico", 
                   "Bowrider", "Trawler", "Iate a motor", "Barco de trabalho", "Lancha", 
                   "Flybridge", "Esqui aquático", "Hardtop", "Barco offshore", "Casa flutuante", 
                   "Barco de passageiros", "Wakeboard/Wakesurf", "Ketch", "Mega Iate", "Motorsailer"]

    data = {
        "Material": [random.choice(materiais) for _ in range(n_amostras)],
        "TipoVenda": [random.choice(tipos_venda) for _ in range(n_amostras)],
        "TipoBarco": [random.choice(tipos_barco) for _ in range(n_amostras)],
        "Comprimento": [round(random.uniform(5, 50), 2) for _ in range(n_amostras)],
        "Largura": [round(random.uniform(2, 15), 2) for _ in range(n_amostras)],
        "Peso": [round(random.uniform(500, 50000), 2) for _ in range(n_amostras)],
        "Preco": [round(random.uniform(10000, 1000000), 2) for _ in range(n_amostras)]
    }

    return pd.DataFrame(data)

def salvar_dataset(dataset: pd.DataFrame, nome_arquivo: str):
    """
    Salva o dataset em um arquivo CSV.

    Args:
        dataset (pd.DataFrame): DataFrame contendo o dataset a ser salvo.
        nome_arquivo (str): Nome do arquivo onde o dataset será salvo.
    """
    dataset.to_csv(nome_arquivo, index=False)

if __name__ == "__main__":
    config = carregar_config("config/config.yaml")
    
    logging.basicConfig(filename=config['logging']['log_file'], level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    n_amostras = config['data']['num_samples']
    dataset_treino = gerar_dataset(n_amostras)
    dataset_teste = gerar_dataset(int(n_amostras * config['data']['test_size']))
    
    salvar_dataset(dataset_treino, "data/dataset_treino.csv")
    salvar_dataset(dataset_teste, "data/dataset_teste.csv")
    
    logging.info("Datasets de treino e teste gerados e salvos com sucesso.")
