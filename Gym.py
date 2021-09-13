from typing import Any
# Clases Pendientes
#import Campus

# Crear clase Gym
class Gym : 

    # Constructor
    def __init__(self, __nit:int, __name:str, __address:str
                , __phone:str, __campus:Any):

        # Datos de entrada
        self.nit = __nit
        self.name = __name
        self.address = __address
        self.phone = __phone
        self.campus = __campus
 
    # Metodos
    def getNit(self):
        return self.nit
    
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address
    
    def getPhone(self):
        return self.phone
    
    def getCampus(self):
        return self.campus

gym1 = Gym(3453, 'Big Boys', 'Malabar', '3189086655','Tipo Campus')

print(f'El nit del gym es {gym1.getNit()}\n') 
print(f'El nombre del Gym es {gym1.getName()}\n')
print(f'La direccion del Gym es {gym1.getAddress()}\n')
print(f'El telefono del Gym es {gym1.getPhone()}\n')
print(f'La sede del Gym es {gym1.getCampus()}\n')
# La clase gym tiene relacion con la clase Campus
        


