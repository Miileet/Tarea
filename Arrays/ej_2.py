#Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida 
#posición y número a guardar al usuario, lo guarde en una lista en la posición 
#solicitada aleatoriamente y la retorne.  El pr



def cargar_listas(lista:list)->list:
    respuesta = "s" 
    while respuesta == "s":
        posicion = int(input("Ingrese la posicion: "))
        numero = int(input("Ingrese un numero: "))
        lista[posicion] = numero
        respuesta = input("inrgesar otro? s/n").lower()
    return lista



def mostrar_lista(lista:list)->list:
    for i in range(len(lista)):
        print(lista[i])



mi_lista = [0] * 10
cargar_listas(mi_lista)
mostrar_lista(mi_lista)