#Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango 
#especificado, validar los números solicitados dentro de ese rango, guardar en una 
#lista y retornarla.  El programa principal debe invocar a la función y mostrar por 
#pantalla el retorno.

def pedir_numeros()->list:
    respuesta = "s"
    lista = []
    while respuesta == "s":
        numeros = int(input("Ingrese un numero: "))
        if  0 <= numeros <= 10:
            lista.append(numeros)
            respuesta = input("Desea seguir cargando datos? \ns/n ").lower()
        else:
            print("respuesta incorrecta, ingrese un numero del 0 al 10")
    return lista
    

print(pedir_numeros())