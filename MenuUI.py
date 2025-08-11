def agregar_numero():
    print("=== Registro de numeros ===")
    while True:
        entrada = input("Ingrese un numero o escriba 'volver' para regresar: ")
        if entrada.lower() == "volver":
            break
    try:
        numero = int(entrada)
        numeros.append(numero)
        print("Se ha agregado el numero exitosamente")
        print(f"Lista actual: {numeros}")
    except ValueError:
        print("Entrada no válida, debe ser un número entero.")


def buscar_numero():
    print("=== Buscar numero ===")
    while True:
        entrada = input("Ingrese un numero o escriba 'volver' para regresar: ")
        if entrada.lower() == "volver":
            break
        try:
            buscar_numeros = int(entrada)
            if buscar_numeros in numeros:
                print(f"Se ha encontrado el numero {buscar_numeros} exitosamente")
            else:
                print(f"No se ha encontrado el numero {buscar_numeros}")
            print(f"Lista actual: {numeros}")
        except ValueError:
            print("Entrada no válida, debe ser un número entero.")


def mostrar_numeros():
    print("=== Mostrar numeros ===")
    for numero in numeros:
        print(numero)


def eliminar_numero():
    print("=== Eliminar numero ===")
    while True:
        entrada = input("Ingrese un numero que desea eliminar: ")
        if entrada.lower() == "volver":
            break
        try:
            numero = int(entrada)
            if numero in numeros:
                numeros.remove(numero)
                print("Se ha eliminado el numero exitosamente")
            else:
                print(f"No se ha encontrado el numero {numero}")
            print(f"Lista actual: {numeros}")
        except ValueError:
            print("Entrada no válida, debe ser un número entero.")


opcion = 0
numeros = []
while opcion != 5:
    print("=== MENU INTERACTIVO ===")
    print("1. Agregar numeros")
    print("2. Buscar numeros")
    print("3. Mostrar numeros")
    print("4. Eliminar numeros")
    print("5. Salir")
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Opcion no valida")
        continue

    match opcion:
        case 1:
            confirmacion = ""
            while confirmacion != "no".lower():
                agregar_numero()
                print("Desea volver a ingresar un numero")
                confirmacion = input("Escriba (si/no): ")

        case 2:
            if len(numeros) > 0:
                confirmacion = ""
                while confirmacion != "no".lower():
                    buscar_numero()
                    print("Desea volver a buscar un numero")
                    confirmacion = input("Escriba (si/no): ")
            else:
                print("=== No hay numeros agregados ===")

        case 3:
            if len(numeros) > 0:
                mostrar_numeros()
            else:
                print("=== No hay numeros agregados ===")

        case 4:
            if len(numeros) > 0:
                confirmacion = ""
                while confirmacion != "no".lower():
                    eliminar_numero()
                    print("Desea volver a eliminar un numero")
                    confirmacion = input("Escriba (si/no): ")
            else:
                print("=== No hay numeros agregados ===")

        case 5:
            print("=== Saliendo del programa ===")
