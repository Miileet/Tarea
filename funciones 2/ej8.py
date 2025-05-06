#Crear una función que (utilizando la función del punto 11 de la guía de For), 
#muestre todos los números primos comprendidos entre entre la unidad y un número 
#ingresado como parámetro. La función retorna la cantidad de números primos 
#encontrados. 



def numeros_primos(num1:int)->int:
    flag = True
    cont_primos = 0
    for i in range(2, num1):
        flag = True
        for j in range(2,i):
            if i % j == 0:
                flag = False
                break 
        if flag:      
            cont_primos +=1
    return cont_primos









numeroo = int(input("Ingrese un numero: "))
print(numeros_primos(numeroo))