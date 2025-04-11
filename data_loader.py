import pandas as pd

def load_data(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
        return df
    except Exception as e:
        raise e
