#Diseña una función que calcule la potencia de un número. La función debe recibir la 
#base y el exponente como argumentos y devolver el resultado. 


def potencia_de_un_num(base:int, exponente:int)->int:
    resultado = base ** exponente
    return resultado


base = int(input("Ingrese un numero: "))
exponente = int(input("Ingrese otro numero: "))


print(potencia_de_un_num(base, exponente))