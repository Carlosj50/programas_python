def run():
    numero = int(input("Ingrese un numero: "))
    contador = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            contador += 1
    if contador == 2:
        print("El numero es primo")
    else:
        print("El numero no es primo")

if __name__=="__main__":
    run()