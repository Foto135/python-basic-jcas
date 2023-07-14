import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('ventas.csv')

# Obtener ventas totales por región y mes
ventas_totales = df.groupby(['Region', 'Mes'])['Ventas'].sum().reset_index()

# Obtener el mes de mayor venta por región con su valor
mayor_mes_ventas_por_region = ventas_totales.groupby('Region').apply(lambda x: x.loc[x['Ventas'].idxmax()])

# Imprimir el resultado
print("El mes de mayor venta por región:")
for _, fila in mayor_mes_ventas_por_region.iterrows():
    region = fila['Region']
    mes = fila['Mes']
    ventas = fila['Ventas']
    print(f"Región: {region}, Mes: {mes}, Ventas: {ventas}")
