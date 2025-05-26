#Limpeza e transformação
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpa e transforma o dataset Titanic.

    - Remove colunas irrelevantes
    - Preenche valores nulos
    - Converte variáveis categóricas

    Args:
        df (pd.DataFrame): DataFrame original

    Returns:
        pd.DataFrame: DataFrame limpo
    """
    df = df.drop(columns=[])
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    # Corrigir o sexo: exemplo para string
    if df['Sex'].dtype == object:
        df['Sex'] = df['Sex'].map({'male': 'Masculino', 'female': 'Feminino'})
    else:
        df['Sex'] = df['Sex'].map({0: 'Masculino', 1: 'Feminino'})
        # Mapear 'Embarked' para números se for string
    if df['Embarked'].dtype == object:
        df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

    return df
