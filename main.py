password_1 = input("¿Digite su comtraseña? : ")

password_2 = input("¿Qué contraseña pusiste anteriormente? : ")

if password_1 == password_2.lower():
    print("La contraseña coincide con la guardad en memoria " + password_1 + ".")
else:
    print("La contraseña no coincide con la guardada.")