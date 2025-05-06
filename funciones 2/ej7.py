#Crear una función que reciba un número y retorne True si el número es primo, False 
#en caso contrario. 


def numeros_primos(n1: int) -> bool:
    if n1 < 2:
        return False
    for i in range(2, n1):
        if n1 % i == 0:
            return False
    return True

numero = int(input("Ingrese un número: "))
print(numeros_primos(numero))
