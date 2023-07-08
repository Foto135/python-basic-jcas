#Recuerda instalar openpyxl: pip install openpyxl
import openpyxl

# Abrir el archivo Excel
libro = openpyxl.load_workbook('datos.xlsx')

# Seleccionar una hoja
hoja = libro['Hoja1']

# Leer datos de celdas
valor_celda = hoja['A1'].value
print(valor_celda)

# Iterar sobre filas
for fila in hoja.iter_rows(min_row=2, values_only=True):
    print(fila)