# Creo diccionario para ver todos los metodos de el mismo.
# Para ver que tipo de class es una funcion, se coloca; print(type(funcion))

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

Diccionario_python = {"Diccionarios" : Metodos_diccionario, "Listas" : Metodos_listas, "Tuplas" : Metodos_tuplas}

menu = """
  \033[1;32mDiccionarios sobre Python (Fyroxl)  \nSelecione el diccionario para consultar\033[1;m\n
1) Metodos_dict (Diccionario)   4) Metodo_nuevo
2) Metodos_list (Listas)        5)
3) Metodos_tuple (Tuplas)       6)
""" ; print(menu) ; n = int(input("\033[1;32mNumero\033[1;m : "))

if n == 1:
    print(Diccionario_python.get("Diccionarios"))
elif n == 2:
    print(Diccionario_python.get("Listas"))
elif n == 3:
    print(Diccionario_python.get("Tuplas"))
else:
    print("Numero invalido.")