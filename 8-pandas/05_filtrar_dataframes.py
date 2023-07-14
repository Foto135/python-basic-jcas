
import pandas as pd

# Cargar el archivo CSV
df = pd.read_excel('Ventas.xlsx')

andina = df['Region'] == 'Andina'
print(andina)

df_filtro_andina = df[andina]
print(df_filtro_andina)
