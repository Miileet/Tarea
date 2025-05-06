#Ejercicio 7: Una startup desea analizar las estadísticas de los usuarios de su sitio de 
#compras on-line recientemente lanzado al mercado para ello necesita un programa 
#que le permita acceder a los datos relevados. 
#Realizar una función con el siguiente Menú de Opciones: 
#1-Importar listas 
#2-Listar los datos de los usuarios de México 
#3-Listar los nombre, mail y teléfono de los usuarios de Brasil 
#4-Listar los datos del/los usuario/s más joven/es 
#5-Obtener un promedio de edad de los usuarios 
#6-De los usuarios de Brasil, listar los datos del usuario de mayor edad 
#7-Listar los datos de los usuarios de México y Brasil cuyo código postal 
#sea mayor a 8000 
#8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 
#años. 





from listas_personas import *

from library import *


def menu_de_opciones():
    desicion = input("Que desea hacer?\nA-Importar listas\nB-Listar los datos de los usuarios de México\nC-Listar los nombre, mail y teléfono de los usuarios de Brasil\nD-Listar los datos del/los usuario/s más joven/es\nE-Obtener un promedio de edad de los usuarios\nF-De los usuarios de Brasil, listar los datos del usuario de mayor edad\nG-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000\nH-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.\n- - - >: ").upper()

    match desicion:
        case "A":
            print("Listas importadas.")
        case "B" :
            mexicanos()
        case "C":
            brasileros()
        case "D":
            determinar_menor()
        case "E":
            promedio()
        case "F": 
            br_mayor()
        case "G":
            brasileros_mexicanos_cp()
        case "H":
            italianos()
        case _:
            print("Ingrese una opcion valida")





menu_de_opciones()