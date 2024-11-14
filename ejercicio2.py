# Solicitar al usuario que ingrese los 10 valores para la lista
lista = [int(input(f"Ingrese el valor {i+1}: ")) for i in range(10)]

# Solicitar al usuario la potencia a calcular
n = int(input("Ingrese el valor de n para calcular la potencia n-ésima: "))

# Calcular la potencia n-ésima de cada elemento en la lista usando lambda y map
resultado = list(map(lambda x: x ** n, lista))

# Imprimir el resultado
print("Lista resultante:", resultado)
