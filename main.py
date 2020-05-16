# Ejercicio de validacion; Correo electronico.

validacion = []

def EmailLoop():
    punto = 0
    arroba = 0
    insertar = False

    email = input("Ingrese su conrreo electronico : ")

    for i in email:
        if i == ".":
            punto = punto + 1
        elif i == "@":
            arroba = arroba + 1

    for i in validacion:
        if i == email:
            print("El correo esta duplicado, ingrese otro.")
            return

    if punto >= 1 and arroba == 1:
        print("El email es correcto.")
        insertar = True
    else:
        print("El email es incorrecto.")

    if insertar:
        validacion.append(email)

loop = True

while loop:
    EmailLoop()
    exit = input("¿Desa salir del ciclo? y/n : ")

    if exit == "y":
        loop = False
    elif exit == "n":
        pass
