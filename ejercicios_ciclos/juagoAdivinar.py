import random

def adivinar(numero,intento):

    if numero < intento:
        print("El numero es menor")
    elif numero > intento:
        print("El numero es mayor")

def main():

    numero = random.randint(1,10)
    intento = 0

    while intento != numero:
        intento = int(input("Ingrese un numero entero "))
        adivinar(numero,intento)

    print("Numero adivinado: ",numero)


if __name__ == "__main__":
    main()