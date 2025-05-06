#Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los 
#guarde en una lista y la retorne.  El programa principal debe invocar a la función y 
#mostrar por pantalla el retorno. 


def guardar_nombres()->list:
    lista_de_nombres = []
    for i in range(3):
        nombres = input("Ingrese un nombre: ")
        lista_de_nombres += [nombres]
    return lista_de_nombres



print(guardar_nombres())

