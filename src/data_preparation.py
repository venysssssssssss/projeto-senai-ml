from sklearn.model_selection import train_test_split

def prepare_data(df, test_size, random_state):
    """Prepara os dados para treinamento, separando as variáveis dependentes e independentes e dividindo em conjuntos de treino e teste."""
    X = df[['Year']]
    y = df['Price']
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
