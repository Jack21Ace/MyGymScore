from typing import Any
# Clases Pendientes
import Campus

# Crear clase Gym
class Gym:

    # Constructor
    def __init__(self, __nit:int, __name:str, __address:str,
                __phone:str, __campus:Campus):

        # Datos de entrada
        self.nit = __nit
        self.name = __name
        self.address = __address
        self.phone = __phone
        self.campus = __campus

# Metodos
    # getter de Nit
    def getNit(self):
        return self.nit

    # Getter and Setter name
    def getName(self):
        return self.name

    def setName(self, __name):
        self.name = __name

    # Getter and Setter address
    def getAddress(self):
        return self.address

    def setAddres(self, __address):
        self.address = __address

    # Getter and Setter phone
    def getPhone(self):
        return self.phone

    def setPhone(self, __phone):
        self.phone = __phone

    # Getter and Setter campus
    def getCampus(self):
        return self.campus

    def setCampus(self, __campus):
        self.campus  = __campus
# End Methods


gym1 = Gym(3453, 'Big Boys', 'Malabar', '3189086655', Campus)
print("==========//==========//==========//==========//==========//==========//==========")
print(f'El nit del gym es {gym1.getNit()}\n'
        f'El nombre del Gym es {gym1.getName()}\n'
        f'La direccion del Gym es {gym1.getAddress()}\n'
        f'El telefono del Gym es {gym1.getPhone()}\n'
        f'La sede del Gym es {gym1.getCampus()}')
