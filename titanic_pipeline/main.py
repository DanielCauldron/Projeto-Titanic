#Executar o pipeline completo
from src.extract import load_raw_data
from src.transform import clean_data
from src.load import save_processed_data

def run_pipeline():
    raw_path = r"E:\Projeto-Titanic\titanic_pipeline\data\raw\train.csv"
    processed_path = r"titanic_pipeline\data\processed\titanic_clean.csv"

    # Etapa 1: Extração
    df_raw = load_raw_data(raw_path)

    # Etapa 2: Transformação
    df_clean = clean_data(df_raw)

    # Etapa 3: Carga
    save_processed_data(df_clean, processed_path)

if __name__ == "__main__":
    run_pipeline()
