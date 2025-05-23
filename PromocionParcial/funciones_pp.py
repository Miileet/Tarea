
def mostrar_matriz(producto:list, venta:list)->any:
    """
    mostrar la matriz
    """
    for i in range(len(producto)):
        print(producto[i], end=": ")
        for j in range(len(venta[i])):
            print(venta[i][j], end=" ")
        print("") 

def mostrar_productos_y_ventas(productos:list, ventas:list)->list:
    """
    Devuelve una lista con los productos y sus ventas totales.
    """
    ventas_trimestrales = [["A", 0], ["B", 0], ["C", 0]]
    for i in range(len(ventas)):
        for j in range(len(ventas[i])):
            ventas_trimestrales[i][1] += ventas[i][j]
    return ventas_trimestrales


def ordenar_ventas_mayor_a_menor(productos:list, ventas:list):
    """
    Ordena y muestra los productos de mayor a menor según ventas totales.
    """
    ventas_totales = mostrar_productos_y_ventas(productos, ventas)
    for i in range(len(ventas_totales) - 1):
        for j in range(1 + i, len(ventas_totales)):
            if ventas_totales[i][1] < ventas_totales[j][1]:
                aux = ventas_totales[i]
                ventas_totales[i] = ventas_totales[j]
                ventas_totales[j] = aux

    for i in range(len(ventas_totales)):
        for j in range(len(ventas_totales[i])):
            print(ventas_totales[i][j])


def buscar_producto(productos:list, ventas:list)->list:
    """
    Muestra las ventas trimestrales de un producto buscado por el usuario.
    """
    encontrado = False
    opcion = input("Que producto desea buscar?\n- - ->: ").upper()
    for i in range(len(productos)):
        if productos[i] == opcion:
            encontrado = True
            print(f"Ventas del producto {opcion}:")
            for j in range(len(ventas[i])):
                print(f"T{j+1}: {ventas[i][j]} mil $")

    if not encontrado:
        print("No se encontro nada")


productos = ["A", "B", "C"]
ventas = [
    [50, 60, 70],
    [80, 55, 45],
    [40, 65, 75]
]

def buscar_valor(ventas:list, productos:list)->any:
    """
    Busca un valor específico e informa en qué producto y trimestre está.
    """
    encontrado = False
    buscar = int(input("Ingrese el valor que desea buscar\n- - ->: "))
    for i in range(len(ventas)):
        for j in range(len(ventas[i])):
            if ventas[i][j] == buscar:
                encontrado = True
                print(f"El valor es de {buscar} mil $ \nel producto es {productos[i]}, y el trimestre seria T{j+1}")

    if encontrado == False:
        print("no se encontro nada")





