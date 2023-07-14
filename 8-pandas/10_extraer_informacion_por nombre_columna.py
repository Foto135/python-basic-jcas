import pandas as pd

df = pd.read_excel('ventas.xlsx')

# Lee el dato de la fila 10, columna Region
print(df.loc[10, "Region"])

# Lee el dato de la fila 24, columna Ventas
print(df.loc[24, "Ventas"])

# Lee el dato de la fila 24, columnas Region y Ventas
print(df.loc[24, ["Region", "Ventas"]])
