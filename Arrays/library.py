from listas_personas import *

def mexicanos():
    datos = []
    for i in range(len(country)):
        if country[i] == "Mexico":
            usuarios += [nombres[i],telefonos[i],mails[i],address[i],postalZip[i],region[i], country[i],edades[i]]
    for usuario in datos:
        print(usuarios)

def brasileros():
    datos = []
    for i in range(len(country)):
        if country[i] == "Brazil":
            usuarios += [nombres[i],telefonos[i],mails[i],address[i],postalZip[i],region[i], country[i],edades[i]]
    for usuario in datos:
        print(usuario)

def determinar_menor():
    menor = 100
    datos = []
    for i in range(len(edades)):
        if edades[i] < menor:
            menor = i
            datos += [nombres[i],telefonos[i],mails[i],address[i],postalZip[i],region[i], country[i],edades[i]]
    for usuario in datos:
        print(usuario)
def promedio():
    edad_gente = 0
    for n in edades:
        edad_gente += n
    cantidad = len(edades)
    if cantidad > 0:
        resultado = edad_gente / cantidad
        print(f"el promedio es de: {resultado}")
    else:
        print("no hay numeros para promediar")

def br_mayor():
    mayor = 0
    datos = []
    for i in range (len(country)):
        if country[i] == "Brazil" and edades[i] > mayor:
            mayor = edades[i]
            datos.append((nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]))
    for usuario in datos:
        print(usuario)

def brasileros_mexicanos_cp():
    datos = []
    for i in range(len(postalZip)):
        if postalZip[i] > 8000 and (country[i] == "Brazil" or country[i] == "Mexico"):
            datos.append((nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]))
    for usuario in datos:
        print(usuario)

def italianos():
    datos = []
    for i in range (len(country)):
        if country[i] == "Italy" and edades[i] > 40:
            datos.append((nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]))

    for usuario in datos:
        print(usuario)