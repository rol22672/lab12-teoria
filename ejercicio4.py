# Solicitar al usuario que ingrese los elementos de la lista inicial
lista_inicial = input("Ingrese los elementos de la lista inicial separados por comas: ").split(',')

# Limpiar espacios adicionales en cada elemento
lista_inicial = [elemento.strip() for elemento in lista_inicial]

# Solicitar al usuario que ingrese los elementos a eliminar
elementos_a_borrar = input("Ingrese los elementos a eliminar separados por comas: ").split(',')

# Limpiar espacios adicionales en cada elemento
elementos_a_borrar = [elemento.strip() for elemento in elementos_a_borrar]

# Filtrar elementos que no están en la lista de elementos a borrar
lista_filtrada = list(filter(lambda x: x not in elementos_a_borrar, lista_inicial))

# Imprimir la lista resultante
print("Lista resultante:", lista_filtrada)
