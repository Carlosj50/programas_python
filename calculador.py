def run():
    print ("Bienvenido a la calculadora de Divisas")
    print ("1. Convertir Pesos a Dolares")
    print ("2. Convertir Dolares a Pesos")
    print ("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        pesos = float(input("Ingrese la cantidad de pesos: "))
        dolares = pesos / 18.36
        print ("La cantidad de dolares es: ", dolares)
    elif opcion == 2:
        dolares = float(input("Ingrese la cantidad de dolares: "))
        pesos = dolares * 18.36
        print ("La cantidad de pesos es: ", pesos)
    elif opcion == 3:
        print ("Gracias por usar la calculadora de Divisas")
    else:
        print ("Opcion invalida")





if __name__=="__main__":
    run()