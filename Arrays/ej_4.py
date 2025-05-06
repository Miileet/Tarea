#Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números 
#y un número especificado.  La misma debe buscar el número especificado en la lista 
#y retornar “True” si existe. 


def buscar_numero(lista:list)->bool:
    numero = int(input("Ingrese un numero que desee buscar: "))
    for i in lista:
        if i == numero:
            return True
            break
    return False












lista_de_numeros = [2, 4, 6 ,8, 9, 10]
print(buscar_numero(lista_de_numeros))

