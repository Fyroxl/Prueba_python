# Creo diccionario para ver todos los metodos de el mismo.
# Para ver que tipo de class es una funcion, se coloca; print(type(funcion))

colores = """
    Negro       0;30     Gris oscuro    1;30
    Azul        0;34     Azul claro     1;34
    Verde       0;32     Verde claro    1;32
    Cyan        0;36     Cyan claro     1;36
    Rojo        0;31     Rojo claro     1;31
    Purpura     0;35     Purpura claro  1;35
    Marron      0;33     Amarillo       1;33
    Gris claro  0;37     blanco         1;37
"""

# Todo sobre Python = https://www.w3schools.com/python/default.asp

Metodos_diccionario = {
    # Estructura de un disccionario = dict{}
    # Los diccionarios llevan el signo de {}
    "Eliminar" : "clear()",
    "Copiar" : "copy()",
    "Asignar" : "fromkeys(iterable, value)",
    "Ver_valor_key" : "get()",
    "Ver_items_tupla" : "items()",
    "Ver_todas_keys" : "keys()",
    "Eliminar_por_key" : "pop()",
    "Eliminar_ultimo_kv" : "popitem()",
    "Ver_valor_kv" : "setdefault()",
    "Actualiza_kv" : "update()",
    "Ver_todos_valores" : "values()"
}

Metodos_tuplas = {
    # Estructura de una tupla = tuple()
    # Las tuplas llevan del signo de ()
    # Tuplas de un item = tuple("Item",)
    "Numero_valores" : "count()",
    "Indice_tupla" : "index()",
    "Eliminar_tupla" : "del tuple",
    "Convertir_tupla_lista" : "list(tuple)",
    "Parametro_valores" : "print(tuple(0:2))"
}

Metodos_listas = {
    # Estructura de una lista = list[]
    # Constructor = list()
    # Las listas lleva el signo []
    "Agnadir_elemento" : "append()",
    "Eliminar_todo" : "claer()",
    "Copiar" : "copy()",
    "Numero_valores" : "count()",
    "Agnadir_elementos" : "extend()",
    "Ver_indice" : "index()",
    "Insertar_elemento_posicion" : "insert()",
    "Eliminar_elemento_posicion" : "pop()",
    "Eliminar_item_valor" : "remove()",
    "Invertir_lista" : "reverse()",
    "Ordenar_lista" : "sort()"
}

Metodos_funcionales = {
    "Exeptuar_mayu_minus" : "lower()"
}


menu = """
  \033[1;32mDiccionarios sobre Python (Fyroxl)  \nSelecione el diccionario para consultar\033[1;m\n
1) Metodos_dict (Diccionario)   4) Metodo_nuevo
2) Metodos_list (Listas)        5) Metodo_nuevo2
3) Metodos_tuple (Tuplas)       6)
""" ; print(menu) ; n = int(input("\033[1;32mNumero\033[1;m : "))

if n == 1:
    for datos in Metodos_diccionario.items():
        print(datos)
elif n == 2:
    for datos in Metodos_listas.items():
        print(datos)
elif n == 3:
    for datos in Metodos_tuplas.items():
        print(datos)
else:
    print("Numero invalido.")