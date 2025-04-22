import os 

def iniciar():
    os.system('cls')

    print("========================")
    print(" BIENVENIDO AL Manager ")
    print("========================")
    print("[1] Listar clientes ")
    print("[2] Buscar cliente ")
    print("[3] Añadir cliente ")
    print("[4] Modificar cliente ")
    print("[5] Borrar cliente ")
    print("[6] Cerrar el Manager ")
    print("========================")

    opcion = input(">")
    os.system ('cls')

    if opcion == "1":
        print("Listado de Clientes")
    if opcion =="2":
        print("Buscar Clientes")
