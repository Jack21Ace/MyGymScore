from typing import Any
import Campus
from Employee import Employee
from Item import Item
from Supplier import Supplier
from Bill import Bill
from Payroll import Payroll
from datetime import date
from Enums import RoleList, Ranking

# Crear clase Gym
class Gym:

    # Constructor
    def __init__(self, __nit:int, __name:str, __address:str, __phone:str, 
                __campusNit:int, __campusName:str, __campusPhone:str, __campusAddress:str, __parking:bool, __sizeParking:int, __inventory:Item, __technicalEmpl:bool, __supplier:Supplier, __bill:Bill, __payroll:Payroll,
                __employeeId:int, __nameEmployee:str,  __salary:float, __role:RoleList, __ranking:Ranking,):

        # Datos de entrada
        self.schempls = []
        self.nit = __nit
        self.name = __name
        self.address = __address
        self.phone = __phone


        # COMPOSICIONES DE GYM

        # Campus
        __campus = Campus()
        __campus.campusNit = __campusNit
        __campus.campusName = __campusName
        __campus.campusPhone = __campusPhone
        __campus.campusAddress = __campusAddress
        __campus.parking = __parking
        __campus.sizeParking = __sizeParking
        __campus.inventory = __inventory
        __campus.technicalEmpl = __technicalEmpl
        __campus.supplier = __supplier
        __campus.bill = __bill
        __campus.payroll = __payroll
        self.objcampus = []
        self.objcampus [0] = __campus


        # Employee
        __employee = Employee()
        __employee.employeeId = __employeeId
        __employee.nameEmployee = __nameEmployee
        __employee.salary = __salary
        __employee.role = __role
        __employee.ranking = __ranking
        self.objemployee = []
        self.objemployee [0] = __employee

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


    # Getter para campus
    def getCampus(self):
        return self.objcampus

    
    # Metodo ADD para Campus
    def addCampus(self, __nit:int, __name:str, __phone:str, __address:str, __parking:bool, __sizeParking:int,
                __inventory:Item, __technicalEmpl:bool, __supplier:Supplier, __bill:Bill, __payroll:Payroll):
        schempl = Campus(self, __nit, __name, __phone, __address, __parking, __sizeParking, __inventory, 
                    __technicalEmpl, __supplier, __bill, __payroll)
        self.schempls.append(schempl)


    # Getter para campus
    def getEmployee(self):
        return self.objemployee



# End Methods


# gym1 = Gym(3453, 'Big Boys', 'Malabar', '3189086655', Campus)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'El nit del gym es {gym1.getNit()}\n'
#         f'El nombre del Gym es {gym1.getName()}\n'
#         f'La direccion del Gym es {gym1.getAddress()}\n'
#         f'El telefono del Gym es {gym1.getPhone()}\n'
#         f'La sede del Gym es {gym1.getCampus()}')
