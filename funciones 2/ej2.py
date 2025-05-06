#Escribe una función que calcule el área de un círculo. La función debe recibir el radio 
#como parámetro y devolver el área. 

def calcular_area_de_un_circulo(n1:int)->float:
    area = 3.14 * n1
    return area

radio = int(input("Ingrese el radio de un circulo: "))
print(calcular_area_de_un_circulo(radio))