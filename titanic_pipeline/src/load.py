#Salvamento dos dados processados
import pandas as pd

def save_processed_data(df: pd.DataFrame, path: str):
    """
    Salva os dados processados em um arquivo CSV.

    Args:
        df (pd.DataFrame): DataFrame limpo
        path (str): Caminho de saída para o CSV
    """
    df.to_csv(path, index=False)
    print(f"Dados salvos em: {path}")
