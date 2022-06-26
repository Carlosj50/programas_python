user = "carlos"
password = "123"

while True:
    user1 = input("Ingrese usuario: ")
    password1 = input("Ingrese contraseña: ")

    if user == user1 and password == password1:
        print("Acceso permitido")
        break
    else:
        print("Acceso denegado")    

