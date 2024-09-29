import pandas as pd
from tabulate import tabulate
import csv

# Paso 1: Cargar el archivo CSV en un DataFrame
df_code = pd.read_csv('sonarcloud_code_smells2.csv')
df_rules = pd.read_csv('rules.csv')
# Paso 2: Obtener los valores únicos de una columna
# Supongamos que la columna se llama 'nombre_columna'
valores_unicos = df_code['Message'].unique()

df_complete = pd.merge(df_code, df_rules, on='rule', how='left')

filename = 'data.csv'
df_complete.to_csv('complete_taxonomy.csv', index=False)

df_count = df_complete.groupby('rule').size().reset_index(name='conteo')
df_count.to_csv('count_rules.csv', index=False)





