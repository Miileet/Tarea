#Ejercicio 5: Dadas las siguientes listas: 
#Nombres =["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"] 
#edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43] 
#Desarrollar una función que reciba por parámetro la lista de edades, busque a las 
#personas de menor edad (puede ser más de una) y las retorne.  El programa 
#principal deberá mostrar nombre y edad de los menores. 



def encontrar_menor(lista:list[int])->list:
    Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"] 
    menor_edad = 100
    nombre = []
    for n in lista:
        if n < menor_edad:
            menor_edad = n
    for i in range(len(lista)):
        if lista[i] == menor_edad:
            nombre += [Nombres[i]]
    return [nombre, menor_edad]




edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
print(encontrar_menor(edades))
