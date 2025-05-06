#Crea una función que verifique si un número dado es par o impar. La función debe 
#imprimir un mensaje indicando si el número es par o impar. 

def determinar_par(n1:int)->str:
    if n1 % 2 == 0:
        print(f"{n1} es par.")
    else:
        print(f"{n1} es impar")


numero = int(input("Ingrese un numero: "))
determinar_par(numero)