def BinarySearchRecursive(Array, left, right, objetive):

    if right >= left:
        mid = round(left + (right - left) / 2)
        if Array[mid] == objetive:
            return mid
        if Array[mid] > objetive:
            return BinarySearchRecursive(Array, left, mid - 1, objetive)

        return BinarySearchRecursive(Array, mid + 1, right, objetive) 
    
    return -1

def Inicio():
    Array = [1, 4, 8, 5, 2, 10, 101, 404]
    objetive = 2
    result = BinarySearchRecursive(Array, 0, len(Array) - 1, objetive)

    if result == -1:
        return print("No se encontro el dato en la lista.")
    else:
        return print("Se encontro el dato en la lista, numero de posición : ", result)


Inicio()