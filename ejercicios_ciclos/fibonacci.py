def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(b)
        c = a+b
        a = b
        b = c

def main():
    serie = int(input("Ingrese la iteración de la serie a la que desea llegar "))
    fibonacci(serie)

if __name__ == "__main__":
    main()