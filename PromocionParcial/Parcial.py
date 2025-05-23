def calcular_promedio(lista, valor)->bool:
    """
    La funcion recibe parametros y acumula el valor total de la lista, para luego dividirla por el total de valores que tiene y sacar el promedio. retorna un booleano 
    """
    acum = 0
    for i in range(len(lista)):
        acum += lista[i]
    promedio = acum / len(lista)
    if promedio > valor:
        return True


entrada = [10, 20, 30, 40,50]
valor = 24
print(calcular_promedio(entrada, valor))
