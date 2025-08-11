def agregar_Numero():
    print("===Registro de numeros===")

opcion =0
while opcion != 5:
    print("===MENU INTERACTIVO===")
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
            agregar_Numero()

