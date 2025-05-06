#Escribir una función que calcule el área de un rectángulo. La función recibe la base y 
#la altura y retorna el área.

def area_de_un_rectangulo(base:int, altura:int)->int:
    area = base * altura
    return area

base = int(input("Ingrese la base del rectangulo: "))
altura = int(input("Ingrese la altura del rectangulo: "))

print(area_de_un_rectangulo(base,altura))