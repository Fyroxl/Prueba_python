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
        print("\033[1;32mEl email es correcto.\033[1;m")
        insertar = True
    else:
        print("\033[1;31mEl email es incorrecto.\033[1;m")

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
