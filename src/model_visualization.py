"""
Módulo para visualização do desempenho do modelo.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_predictions(y_true, y_pred):
    """
    Plota os valores reais versus os valores preditos.

    Args:
        y_true (pd.Series): Valores reais.
        y_pred (pd.Series): Valores preditos.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(y_true, y_pred, alpha=0.5, label='Valores preditos')
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', lw=2, label='Linha de perfeição')
    plt.xlabel("Valores Reais")
    plt.ylabel("Valores Preditos")
    plt.title("Valores Reais vs. Valores Preditos")
    plt.legend()
    plt.grid(True)
    plt.annotate('Cada ponto representa uma previsão', xy=(0.05, 0.95), xycoords='axes fraction', fontsize=10,
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"))
    plt.show()

def plot_residuals(y_true, y_pred):
    """
    Plota os resíduos (erros) do modelo.

    Args:
        y_true (pd.Series): Valores reais.
        y_pred (pd.Series): Valores preditos.
    """
    residuals = y_true - y_pred
    plt.figure(figsize=(10, 6))
    sns.histplot(residuals, kde=True, color='blue')
    plt.axvline(0, color='red', linestyle='--', label='Zero Residual')
    plt.xlabel("Resíduos")
    plt.ylabel("Contagem")
    plt.title("Distribuição dos Resíduos")
    plt.legend()
    plt.grid(True)
    plt.annotate('Resíduo = Valor Real - Valor Predito', xy=(0.05, 0.95), xycoords='axes fraction', fontsize=10,
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"))
    plt.show()

def plot_feature_importances(model, feature_names):
    """
    Plota a importância das features do modelo.

    Args:
        model (Pipeline): Modelo treinado.
        feature_names (list): Lista com os nomes das features.
    """
    importances = model.named_steps['regressor'].feature_importances_
    indices = np.argsort(importances)[::-1]

    plt.figure(figsize=(16, 10))
    plt.title("Importância das Features")
    plt.bar(range(len(importances)), importances[indices], align="center")
    plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=90)
    plt.xlabel("Features")
    plt.ylabel("Importância")
    plt.grid(True)
    plt.tight_layout()
    plt.annotate('Importância de cada feature no modelo', xy=(0.05, 0.95), xycoords='axes fraction', fontsize=10,
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"))
    plt.show()
