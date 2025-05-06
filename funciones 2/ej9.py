#Crear una función que imprima la tabla de multiplicar de un número recibido como 
#parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir 
#el rango de multiplicación. Por defecto es del 1 al 10.


def tabla_de_multiplicar(num1:int):
    print(f"La tabla del {num1} es : ")
    for i in range(1, 10+1):
        resultado = i * num1
        print(f"{num1} x {i} = {resultado}")



numero = int(input("Ingrese un numero: "))
tabla_de_multiplicar(numero)

