# ejericicio de for
# for numero in range(6):
#     print(numero, numero * " hola mundo")

buscar = 4
for numero in range(6):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontre el numero buscado :(")

for char in "Ultimate python":
    print(char)
