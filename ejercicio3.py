# Definir el tamaño de la matriz
filas = 3
columnas = 4

# Solicitar al usuario que ingrese los valores de la matriz fila por fila
X = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))
        fila.append(valor)
    X.append(fila)

# Calcular la transpuesta usando zip y una lambda
X_transpuesta = list(map(lambda *row: list(row), *X))

# Imprimir la matriz transpuesta
print("Matriz transpuesta:")
for fila in X_transpuesta:
    print(fila)
