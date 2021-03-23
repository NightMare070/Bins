#Modulos
import os
import msvcrt as m

#Limpieza
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#Enter
def wait():
    print("Presione cualquier tecla para continuar...")
    m.getch()

#Variables
Bin1 = "a"
Bin2 = "b"
op = -1

print("Bienvenido")
print("Script creado por: ")
print(" ")

print(" ███▄    █  ██▓  ▄████  ██░ ██ ▄▄▄█████▓")
print(" ██ ▀█   █ ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒")
print("▓██  ▀█ ██▒▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░")
print("▓██▒  ▐▌██▒░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░ ")
print("▒██░   ▓██░░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ ")
print("░ ▒░   ▒ ▒ ░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   ")
print("░ ░░   ░ ▒░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░    ")
print("   ░   ░ ░  ▒ ░░ ░   ░  ░  ░░ ░  ░      ")
print("         ░  ░        ░  ░  ░  ░         ")
print(" ")

while op != 0:
#Menu

    print("Que deseas hacer?...")
    print(" ")
    print("1. Forma basica(sustitución de ultimos digitos)")
    print("2. Similitud")
    print("3. Metodo Sofia")
    print("4. Indentación lógica")
    print("0. Salir")
    print(" ")
    op = int(input("Digite la opción deseada: "))
    print(" ")

#Opciones

#Opcion invalida
    if op < 0 or op > 4:
        clear()
        print("Opción invalida, intente de nuevo...")
        wait()
        clear()

#Basico

    if op == 1:
        clear()
        CC = str(input("Digite su CC a extrapolar(sin espacios): "))
        extra = CC[0:10]
        print(" ")
        print("Tu BIN extrapolado es " + extra + "xxxxxx")
        wait()
        clear()

#Similitud

    if op == 2:
        clear()
        print("Se necesitan 2 CCs del mismo BIN")
        print(" ")
        while Bin1 != Bin2:
            CC1 = str(input("Digite su primer CC(sin espacios): "))
            CC2 = str(input("Digite su segunda CC(sin espacios): "))
            Bin1 = CC1[0:6]
            Bin2 = CC2[0:6]
            if Bin1 != Bin2:
                print("Los bins no coinciden, intente de nuevo...")
                print(" ")
        ex1 = str(CC1[6:])
        ex2 = str(CC2[6:])
        extra = ""
        for n in range(10):
            d1 = ex1[n]
            d2 = ex2[n]
            if d1 == d2:
                extra += d1
            else:
                extra += "x"
        print("Tu BIN extrapolado es " + Bin1 + extra)
        wait()
        clear()

#Metodo Sofia

    if op == 3:
        clear()
        print("Se necesitan 2 CCs del mismo BIN")
        print(" ")
        while Bin1 != Bin2:
            CC1 = str(input("Digite su primer CC(sin espacios): "))
            CC2 = str(input("Digite su segunda CC(sin espacios): "))
            Bin1 = CC1[0:6]
            Bin2 = CC2[0:6]
            if Bin1 != Bin2:
                print("Los bins no coinciden, intente de nuevo...")
                print(" ")
    
    #Proceso
        n11 = int(CC1[9])
        n12 = int(CC1[10])
        n21 = int(CC2[9])
        n22 = int(CC2[10])

        res1 = n11 + n21
        res2 = n12 + n22
        res1 /= 2
        res2 /= 2
        res1 *= 5
        res2 *= 5
        res = int(res1) + int(res2)

        print("Tu Bin extrapolado es: " + Bin1 + res + "xxxxxx")
        wait()
        clear()

#Identación lógica

    if op == 4:
        clear()
        CC = str(input("Digite su CC a extrapolar(sin espacios): "))
        Bin = CC[0:6]
        ext = CC[6:]
        extra = ""
        for n in range(0, 10):
            if n == 1 or n == 4 or n == 5 or n == 8:
                extra += "x"
                n += 1
            else:
                extra += ext[n]
        print("Tu Bin extrapolado es " + Bin + extra)
        wait()
        clear()

#Salir

    if op == 0:
        clear()
        print("Gracias, vuelve pronto...")