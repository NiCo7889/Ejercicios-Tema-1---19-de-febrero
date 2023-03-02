import helpers

def iniciar():
    while True:
        helpers.system('cls') # cls en Windows

        print("========================")
        print("  Ejercicios a resolver ")
        print("========================")
        print("[1] Ejercicio 1         ")
        print("[2] Ejercicio 2         ")
        print("[3] Ejercicio 3         ")
        print("[4] Ejercicio 4         ")
        print("[5] Ejercicio 5         ")
        print("[6] Ejercicio 6         ")
        print("[7] Ejercicio 7         ")
        print("========================")

        opcion = input("> ")
        helpers.system('cls') # cls en Windows

        if opcion == '1':
            print("Ejercicio 1...\n")
        if opcion == '2':
            print("Ejercicio 2...\n")
        if opcion == '3':
            print("Ejercicio 3...\n")
        if opcion == '4':
            print("Ejercicio 4...\n")
        if opcion == '5':
            print("Ejercicio 5...\n")
        if opcion == '6':
            print("Ejercicio 6...\n")
        if opcion == '7':
            print("Ejercicio 7...\n")
            break

        input("\nPresiona ENTER para continuar...")


