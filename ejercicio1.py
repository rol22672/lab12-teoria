# Lista de diccionarios
D = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Apple', 'model': 2, 'color': 'Silver'},
    {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# Solicitar al usuario la clave para ordenar
key = input("Ingrese la clave por la cual desea ordenar (e.g., 'make', 'model', 'color'): ")

# Ordenar la lista de diccionarios por la clave ingresada
try:
    D_ordenado = sorted(D, key=lambda x: x[key])
    # Imprimir el resultado
    for item in D_ordenado:
        print(item)
except KeyError:
    print(f"La clave '{key}' no existe en los diccionarios.")
