# print("hola mundo") #imprime en la consola un mensaje o sprint
def hola(nombre, apellido="vuela"):
    print("hola mundo")  # esto es parametros
    print(f"bienvenido {nombre} {apellido}")


hola("dilan", "soler")  # esto es argumentos
hola("pajaro")


hola(apellido="soler", nombre="dilan")
