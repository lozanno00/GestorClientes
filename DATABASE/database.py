class Cliente:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f"Nombre:{self.nombre}, Apellido:{self.apellido}, DNI:{self.dni}"
    
class Clientes:

    lista = []

    def buscar_clientes(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
             return cliente 