def factorial():
    n = int(input("Ingrese un número: "))
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print("Factorial de", n, "es", fact)

factorial()