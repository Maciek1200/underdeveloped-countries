import pandas as pd

def get_sorted_dataframe(filename):
    df = pd.read_csv(filename, sep=';', encoding='ISO-8859-1')
    df = df.sort_values(by=['municipio_distrito', 'fecha_informe'])
    return df
