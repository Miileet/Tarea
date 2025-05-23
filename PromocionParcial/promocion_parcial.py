from funciones_pp import *
#datos iniciales
productos = ["A", "B", "C"]
ventas = [
    [50, 60, 70], #A
    [80, 55, 45], #B
    [40, 65, 75]  #C
        ]



print("MENU DE OPCIONES")
opciones = 0
while opciones == 0:
    opciones = int(input("1.Mostrar productos y ventas\n2.Ordenar productos por ventas anuales\n3.Buscar producto por nombre\n4.Buscar monto de venta en la matriz\n5.Salir\n- - ->:   "))
    match opciones:
        case 1:
            mostrar_matriz(productos, ventas)
            opciones = int(input("ingrese 0 para continuar o 5 para salir.\n- - ->: "))
        case 2:
            ordenar_ventas_mayor_a_menor(productos, ventas)
            opciones = int(input("ingrese 0 para continuar o 5 para salir.\n- - ->: "))
        case 3:
            buscar_producto(productos, ventas)
            opciones = int(input("ingrese 0 para continuar o 5 para salir.\n- - ->: "))
        case 4:
            buscar_valor(ventas, productos)
            opciones = int(input("ingrese 0 para continuar o 5 para salir.\n- - ->: "))
        case 5:
            break
        case _:
            print("Opcion invalida.")