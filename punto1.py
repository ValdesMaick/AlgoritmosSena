"""
1. Desarrollar un programa que permita calcular el área o perímetro 
de algunas figuras planas según la siguiente tabla:

Triangulo
Paralelogramo
Cuadrado
Circunferencia
"""


print("Programaparacalcular Area o Perimetro")

print("Menu")
print("Opcion 1: triangulo")
print("Opcion 2: rectangulo")
print("Opcion 3: cuadrado")
print("Opcion 4: circulo")
print("Opcion 0: salir")


opcion = int(input("Digite una opcion: "))

while opcion < 0 and opcion > 4 :
    opcion = int(input("Error!. Digite una opcion valida: "))

while opcion != 0 :
    if opcion == 1:
        print("::::triangulo::::")
        print("Opcion 1: Area")
        print("Opcion 2: Perimetro")
        opc = int(input("Digite una opcion: "))
        if opc == 1:
            print("::Perimetro del triangulo::")
            ladoA = float(input("Dijite el lado 'a'"))
            ladoB = float(input("Dijite el lado 'b'"))
            ladoC = float(input("Dijite el lado 'c'"))
            perimetro = ladoA + ladoB + ladoC
            print(f"El perimetro deltriangulo es: {perimetro}")
        if opc == 2:
            print("::Area del triangulo::")
            base = float(input("Digite la base: "))
            altura = float(input("Digite la altura: "))
            area = (base * altura) / 2
            print(f"El area del triangulo es: {area}")
        else:
            opcion = int(input("Error!. Digite una opcion valida: "))
    if opcion == 2:
        print("::Rectangulo::")
        print("Opcion 1: Perimetro")
        print("Opcion 2: Area")
        opc = int(input("Dijite una opcion: "))
        if opc == 1:
            print("::Perimetro del Rectangulo::")
            base = float(input("Digite la base: "))
            altura = float(input("Digite la altura: "))
            perimetro = 2 * (base + altura)
            print(f"El perimetro deltriangulo es: {perimetro}")
        if opc == 2:
            print("::Area del Rectangulo::")
            base = float(input("Digite la base: "))
            altura = float(input("Digite la altura: "))
            area = (base * altura)
            print(f"El area del triangulo es: {area}")
        else:
            opcion = int(input("Error!. Digite una opcion valida: "))
    if opcion == 3:
        print("::Cuadrado::")
        print("Opcion 1: Perimetro")
        print("Opcion 2: Area")
        opc = int(input("Dijite una opcion: "))
        if opc == 1:
            print("::Perimetro del Rectangulo::")
            altura = float(input("Digite la altura: "))
            perimetro = 4 * (altura)
            print(f"El perimetro del cuadrado es: {perimetro}")
        if opc == 2:
            print("::Area del Cuadrado::")
            altura = float(input("Digite la altura: "))
            area = altura**2
            print(f"El area del Cuadrado es: {area}")
        else:
            opcion = int(input("Error!. Digite una opcion valida: "))
    if opcion == 4:
        print("::Circulo::")
        print("Opcion 1: Perimetro")
        print("Opcion 2: Area")
        opc = int(input("Dijite una opcion: "))
        if opc == 1:
            print("::Perimetro del Circulo::")
            radio = float(input("Digite el radio: "))
            perimetro = 2 * 3.1416 * radio
            print(f"El perimetro del Circulo es: {perimetro}")
        if opc == 2:
            print("::Area del Circulo::")
            radio = float(input("Digite el radio: "))
            area = 3.1416 * (radio**2)
            print(f"El area del Circulo es: {area}")
        else:
            opcion = int(input("Error!. Digite una opcion valida: "))

    print("Menu")
    print("Opcion 1: triangulo")
    print("Opcion 2: rectangulo")
    print("Opcion 3: cuadrado")
    print("Opcion 4: circulo")
    print("Opcion 0: salir")
    opcion = int(input("Digite una opcion: "))

print("¡Hasta luego!")