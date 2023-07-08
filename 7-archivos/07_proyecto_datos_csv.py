
with open('ventas_libros.csv', 'r') as archivo:
    ventas_por_mes = {}
    for linea in archivo:
        mes, libro, cantidad = linea.strip().split(',')

        #if isinstance(cantidad, int):
        if cantidad != 'cantidad':
            if mes not in ventas_por_mes:
                ventas_por_mes[mes] = {}
            if libro not in ventas_por_mes[mes]:
                ventas_por_mes[mes][libro] = int(cantidad)
            else:
                ventas_por_mes[mes][libro] += int(cantidad)

# Encontrar el libro más vendido por mes
for mes, libros in ventas_por_mes.items():
    libro_mas_vendido = max(libros, key=libros.get)
    print(f"El libro más vendido en {mes} fue: {libro_mas_vendido}")
