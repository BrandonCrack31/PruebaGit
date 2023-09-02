entrada_1 = input("Ingrese el tipo de pirámide: ")
entrada_2 = int(input("Ingrese los niveles de la pirámide: "))
entrada_3 = input("Ingrese el caracter que desea que tenga el tipo de pirámide: ")

if entrada_1 == "Piramide   Inferior":
    for fila in range(entrada_2):
        for columna in range(fila + 1):
            print(entrada_3, end="")
        print()

if entrada_1 == "Piramide Superior":
    for fila in range(entrada_2):
        for columna in range(entrada_2 - fila):
            print(entrada_3, end="")