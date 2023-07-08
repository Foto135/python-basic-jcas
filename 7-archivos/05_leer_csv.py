import csv

with open('ventas_libros.csv', 'r') as archivo:
    lector_csv = csv.reader(archivo)
    encabezados = next(lector_csv)
    for fila in lector_csv:
        print(fila)