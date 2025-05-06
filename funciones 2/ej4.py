#Crea una función que verifique si un número dado es par o impar. La función retorna 
#True si el número es par, False en caso contrario. 


def determinar_par(n1:int)->bool:
    if n1 % 2 == 0:
        return True
    else:
        return False


numero = int(input("Ingrese un numero: "))
print(determinar_par(numero))