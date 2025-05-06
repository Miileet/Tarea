#Define una función que encuentre el máximo de tres números. La función debe 
#aceptar tres argumentos y devolver el número más grande.



def determinar_num_mas_alto(n1:int, n2:int, n3:int)->int:
    num_mayor = n1
    if n2 > n1:
        num_mayor = n2
    if n3 > num_mayor:
        num_mayor = n3
    return num_mayor



numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un numero: "))
numero3 = int(input("Ingrese un numero: "))

print(determinar_num_mas_alto(numero1,numero2,numero3))