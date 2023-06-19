'''
Desarrollar un programa que permita almacenar las edades de un grupo de 10 personas en un vector de enteros y luego determine la cantidad de personas que son menores de edad, mayores de edad, cuántos adultos mayores, la edad más baja, la edad más alta y el promedio de edades ingresadas. Para el ejercicio anterior suponga que un adulto mayor debe tener una edad igual o superior a 60. Debe validar para cada ingreso que los valores estén en un rango entre 1 y 120 años. En caso de error deberá notificar y solicitar un nuevo valor.
'''

def contar_edades(lista):
    menores = 0
    mayores = 0
    adulto_mayor = 0
    suma = sum(lista)
    for i in lista:
        if i >= 1 and i < 18:
            menores += 1
        if i >= 18 and i <= 120:
            mayores += 1
        if i >= 60 and i <= 120:
            adulto_mayor += 1
                    
        promedio = suma /len(lista)
    return menores, mayores, adulto_mayor, promedio

print("Ingresa las edades entre 1 y 120 años")
edad = []  
#creo la lista vacia 

for i in range(10):
    #hago un ciclo "for" para solicitar 10 veces las edades
    elemento = int(input("Ingrese la edad " + str(i+1) + ": "))
    #le agrego "str(i+1)" para que por pantalla me solicite la edad + 1
    
    while elemento <= 0 or elemento > 120:  
    # el ciclo "while" identado en el "for" hace que cuando declaro el rando de las edades en caso de que se ingrese una edad fuera del rango muestre error las veces que sea necesario
        elemento = int(input("Error! Ingrese una edad valida  " + str(i+1) + ": "))
    
    else:
        edad.append(elemento) 
        # si la edad es la corecta la agrega a la lista edad

print(f"Lista de edades: {edad}")

promedio = contar_edades(edad)
# no se por que al llamar la funcion me da el rando de las edades jajajaja

edad_baja = min(edad)
edad_alta = max(edad) 

    

cantidad_menores, cantidad_mayores, cantidad_adulto_mayor, promedio = contar_edades(edad) 


print(f"La cantidad de menores de edad es de: {cantidad_menores} personas.")

print(f"La cantidad de mayores de edad es de: {cantidad_mayores} personas.")

print(f"La cantidad de adultos mayores es de: {cantidad_adulto_mayor} personas.")

print(f"la edad mas baja es: {edad_baja} años.")

print(f"La edad mas alta es: {edad_alta} años.")

print(f"El promedio de edad es de: {promedio} años.")





 
 

