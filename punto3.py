'''
Escriba un programa que lea dos vectores de números enteros ordenados ascendentemente y luego produzca la lista ordenada de la mezcla de los dos, por ejemplo, si los dos arreglos tienen los números 1 3 6 9 17 y 2 4 10 17, respectivamente, la lista de números en la pantalla debe ser 1 2 3 4 6 9 10 17 17. Limite los vectores a un tamaño de 5 y debe validar en cada ingreso que realmente se estén ingresando los datos de forma ascendente.
'''

def ordenar_listas (lista1, lista2):
    unir_listas = lista1 + lista2
    unir_listas.sort()
    return unir_listas


lista1 = []
lista2 = []

print("\nIngrese los numeros de forma ascendente! 'Lista 1'\n")
ref = -1
for i in range(5):
    numeros = int(input("Ingrese el " + str(i+1) + " numero: "))
    if numeros >= ref:
        lista1.append(numeros)
        ref = numeros
        
    else:
        print(int(input("Error!! ingrese los numeros de forma ascendente " + str(i+1) + ": ")))
            


print("\nIngrese los numeros de forma ascendente! 'Lista 2'\n")
ref2 = -1
for i in range(5):
    numeros2 = int(input("Ingrese el " + str(i+1) + " numero: "))
    if numeros2 >= ref2:
        lista2.append(numeros2)
        ref = numeros2
        
    else:
        print(int(input("Error!! ingrese los numeros de forma ascendente " + str(i+1) + ": ")))

print(f"Lista 1 {lista1}")
print(f"Lista 2 {lista2}")


unir_listas = ordenar_listas(lista1, lista2)


print(f"\nlista de forma ascendente: {unir_listas}")