Repartido = {}

def Quick_sort(lista):
    if len(lista) < 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista[1:] if x > pivote]

        return Quick_sort(menores) + iguales + Quick_sort(mayores)

while True:
    print(f"\nBienvenido")
    print("1. Ingresar repartidor")
    print("2. Ordenamiento de repartidor")
    print("3. Salir")

    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        Cantidad = int(input("Ingrese cantidad de repartidores: "))
        for i in range(Cantidad):
            print(f"\nRepartidor {i + 1}")
            Nombre = input("Ingrese nombre: ")
            Paquete = int(input("Ingrese la cantidad de paquete que desea: "))
            Zona = input("Ingrese zona: ")
            Repartido[Nombre] = {
                "Paquete": Paquete,
                "Zona": Zona
            }
    elif opcion == "2":
        print()