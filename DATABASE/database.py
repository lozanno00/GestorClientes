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
            
    
def crear(nombre, apellido, dni):
    cliente = Cliente(nombre, apellido, dni)
    Clientes.lista.append(cliente)
    return cliente

def modificar(nombre, apellido, dni):
    for i, cliente in enumerate(Clientes.lista):
        if cliente.dni == dni:
            Clientes.lista[i].nombre = nombre
            Clientes.lista[i].apellido = apellido
            return Clientes.lista[i]
        
def eliminar(dni):
    for i, cliente in enumerate(Clientes.lista):
        if cliente.dni == dni:
            cliente = Cliente.lista.pop(i)
            return cliente 