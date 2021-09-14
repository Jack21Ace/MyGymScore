# Import de las clases dependientes
from typing import Any

# Imports
import Bill
import Payroll
import Item
import Supplier

# Creacion de clase Campus
class Campus:
    # Instancia del constructor "__init__"
    def __init__(self, __nit:int, __name:str, __phone:str, __address:str, __parking:bool, __sizeParking:int,
                __inventory:Item, __technicalEmpl:bool, __supplier:Supplier, __bill:Bill, __payroll:Payroll):
        self.nit = __nit
        self.name = __name
        self.phone = __phone
        self.address = __address
        self.parking = __parking
        self.sizeParking = __sizeParking
        self.inventory = __inventory
        self.technicalEmpl = __technicalEmpl
        self.supplier = __supplier
        self.bill = __bill
        self.payroll = __payroll

# getter && setter STARTS
    # Getter para nit
    def getNit(self):
        return self.nit

    # Getter && Setter para name
    def getName(self):
        return self.name

    def setName(self, __name):
        self.name = __name

    # Getter && Setter para phone
    def getPhone(self):
        return self.phone

    def setPhone(self, __phone):
        self.phone = __phone

    # Getter && Setter para address
    def getAddress(self):
        return self.address

    def setAddress(self, __address):
        self.address = __address

    # Getter && Setter para parking
    def getParking(self):
        return self.parking

    def setParking(self, __parking):
        self.parking = __parking

    # Getter && Setter para sizeParking
    def getSizeParking(self):
        return self.sizeParking

    def setSizeParking(self, __sizeParking):
        self.sizeParking = __sizeParking

    # Getter && Setter para inventory
    def getInventory(self):
        return self.inventory

    def setInventory(self, __inventory):
        self.inventory = __inventory

    # Getter && Setter para technicalEmpl
    def getTechnicalEmpl(self):
        return self.technicalEmpl

    def setTechnicalEmpl(self, __technicalEmpl):
        self.technicalEmpl = __technicalEmpl

    # Getter && Setter para supplier
    def getSupplier(self):
        return self.supplier

    def setSupplier(self, __supplier):
        self.supplier = __supplier

    # Getter && Setter para bill
    def getBill(self):
        return self.bill

    def setBill(self, __bill):
        self.bill = __bill

    # Getter && Setter para payroll
    def getPayroll(self):
        return self.payroll

    def setPayroll(self, __payroll):
        self.payroll = __payroll
# getter && setter ENDS

# Aqui la instancia de la clase Campus
# campus = Campus(96348512, 'Iron GYM', '(606) 725-8569', 'KR 48 # 64-28 piso 1', True, 10, Item, False, Supplier, Bill, Payroll)
# Test
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"Nombre de la sede {campus.getName()}\nY su numero de telefono es {campus.getPhone()}\n"+
# f"Si la pregunta es si el GYM tiene parqueadero, la respuesta es: {campus.getParking()}\n"+
# f"Su capacidad es {campus.getSizeParking()}.")