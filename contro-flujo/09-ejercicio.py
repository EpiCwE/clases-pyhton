# numero = 20

# n1 = input("Ingresa numero")
# n2 = input("Ingresa operacion")
# n3 = input("Ingresa numero")

# n1 = int(n1)
# n2 = int(n2)
# n3 = int(n3)

# suma = n1 + n3
# resta = n1 - n3
# multiplicacion = n1 * n3
# division = 1 / n3

# mensaje f"""

print("Bienvenidos ala calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, mult, divi")

resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("ingresa operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("ingresa siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "mult":
        resultado *= n2
    elif op.lower() == "divi":
        resultado /= n2
    else:
        print("operacion no valida")
        break
    print(f"el resultado es {resultado}")
