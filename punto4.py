# Método para agregar personas a la lista
def agregar_persona():

    persona = { # Diccionario padre
        "nombre": "",
        "cedula": "",
        "fecha_de_nacimiento": "",
        "email": "",
        "ciudad_de_residencia": "",
        "ciudad_de_origen": "",
        "canciones_favoritas":{ # Diccionario hijo
            "artista_1": "",
            "titulo_1": "",
            "artista_2": "",
            "titulo_2": "",
            "artista_3": "",
            "titulo_3": ""
        }
    }
    personas = []
    print(f"Digite los datos de la persona: ")
    print("\n")
    for clave in persona:
        #Como no puedo recorrer un diccionario anidado, se hace necesario hacer una pausa para luego iterarlo por separado
        if clave == "canciones_favoritas":
            continue # Cuando llegue a diccionario hijo se pausa la iteracción
        else:
            clave2 = clave.split("_") 
            clave2 = " ".join(clave2).capitalize() # La linea anterior y esta son para que la impresión de la clave sea más legible, ej: en vez de fecha_de_nacimiento queda Fecha de nacimiento
            persona[clave] = input(f"Ingrese {clave2}: ") # Lleno los datos del diccionario padre
    for clave in persona["canciones_favoritas"]:
            clave2 = clave.split("_")
            clave2 = " ".join(clave2).capitalize()
            persona["canciones_favoritas"][clave] = input(f"Ingrese {clave2}: ") # Lleno los datos del diccionario hijo
    print("\n")
    personas.append(persona)
    return personas



# Método para mostrar personas
def mostrar_persona(personas):
    posicion = int(input(f"Digite la posición de la persona a mostrar entre 0 y {len(personas)-1}: "))
    print("\n")
    while posicion < 0 or posicion >= len(personas): #Si se ingresa una pocisión de la lista que no existe entra aquí
        print("¡Error! Digitaste una posición inválida")
        posicion = int(input(f"Digite la posición de la persona a mostrar entre 0 y {len(personas)-1}: "))
        print("\n")
    mostrar_persona = personas[posicion] # Extraigo el diccionario según la posición de lista que haya escogido
    print("Datos de la persona: ")
    for clave, valor in mostrar_persona.items(): # Recorro la clave y valor de cada item del diccionario
        #Como no puedo recorrer un diccionario anidado, se hace necesario hacer una pausa para luego iterarlo por separado
        if clave == "canciones_favoritas": 
                continue
        else:
            clave2 = clave.split("_")
            clave2 = " ".join(clave2).capitalize()
            print(clave2 + ":", valor)
    print("\n")
    canciones = mostrar_persona["canciones_favoritas"] #Extraigo el diccionario hijo
    print("Canciones favoritas:")
    for clave, valor in canciones.items(): # Recorro la clave y valor de cada item del diccionario
        clave2 = clave.split("_")
        clave2 = " ".join(clave2).capitalize()
        print(clave2 + ":", valor)
    print("\n")
        


# Menu
continuar = True   
personas = []
while continuar:
    print("::Menu::".center(20))
    print("Opción 1: Agregar persona ")
    print("Opción 2: Mostrar persona ")
    print("Opción 3: Salir ")
    opcion = int(input("Digite una opción: "))
    print("\n")

    if opcion == 1:
        personas.extend(agregar_persona()) #Uso extend para agregar a la lista
    elif opcion == 2:
        if not personas:
             print("No ha ingresado personas, vuelva a empezar")
             print("\n")
        else:
            mostrar_persona(personas)
    elif opcion == 3:
        continuar = False
    else:
        print("Opción inválida. Por favor, elija una opción válida.")
        print("\n")