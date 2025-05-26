#Coleta de dados do Titanic#
import pandas as pd

def load_raw_data(path: str) -> pd.DataFrame:
    """
    Carrega o dataset bruto a partir de um arquivo CSV.

    Args:
        path (str): Caminho para o arquivo CSV.

    Returns:
        pd.DataFrame: DataFrame com os dados carregados.
    """
    df = pd.read_csv(path)
    print(f"Dados carregados com {df.shape[0]} linhas e {df.shape[1]} colunas.")
    return df