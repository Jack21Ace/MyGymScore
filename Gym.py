from typing import List
from Campus import Campus
from Employee import Employee
from Item import Item
from Supplier import Supplier
from Bill import Bill
from Payroll import Payroll
from Enums import Ranking, RoleList
from EmployeeSchedule import EmployeeSchedule


# Crear clase Gym
class Gym:

    # Constructor
    def __init__(self, __nit:int, __name:str, __address:str, __phone:str, 
                __campus:Campus, __listCampus:List[Campus], __employee:Employee, __listEmployee:List[Employee]):

        # Datos de entrada
        self.__nit = __nit
        self.__name = __name
        self.__address = __address
        self.__phone = __phone
        self.__campus = __campus
        self.__listCampus = __listCampus
        self.__listCampus:List[Campus] = []
        self.__employee = __employee
        self.__listEmployee = __listEmployee
        self.__listEmployee:List[Employee] = []

# Metodos
    # getter de Nit
    def getNit(self):
        return self.__nit


    # Getter and Setter name
    def getName(self):
        return self.__name

    def setName(self, __name:str):
        self.__name = __name


    # Getter and Setter address
    def getAddress(self):
        return self.__address

    def setAddres(self, __address:str):
        self.__address = __address


    # Getter and Setter phone
    def getPhone(self):
        return self.__phone

    def setPhone(self, __phone:str):
        self.__phone = __phone


    # Getter and Setter para campus
    def getCampus(self):
        return self.__campus

    def setCampus(self, __campus:str):
        self.__campus = __campus

    # Getter and Setter para listCampus
    def getListCampus(self):
        return self.__listCampus

    def setListCampus(self, __listCampus:str):
        self.__listCampus = __listCampus


    # Metodo ADD para Campus
    def addCampus(self, __nit:int, __name:str, __phone:str, __address:str, __parking:bool, __sizeParking:int,
                __inventory:Item, __technicalEmpl:bool, __supplier:Supplier, __bill:Bill, __payroll:Payroll):
        __listCampus = Campus(self, __nit, __name, __phone, __address, __parking, __sizeParking, __inventory,
                    __technicalEmpl, __supplier, __bill, __payroll)
        self.__listCampus.append(__listCampus)


    # Getter and Setter para Employee
    def getEmployee(self):
        return self.__employee

    def setEmployee(self, __employee):
        self.__employee = __employee


    # Getter and Setter para listEmployee
    def getListEmployee(self):
        return self.__listEmployee

    def setListEmployee(self, __listEmployee):
        self.__listEmployee = __listEmployee


    # Metodo ADD para Employee
    def addEmployee(self, __employeeId:int, __nameEmployee:str,  __salary:float, __role:RoleList, __payRoll:Payroll,
            __ranking:List[Ranking], __listRanking:List[Ranking], __scheduleEmpl:EmployeeSchedule, __listScheduleEmpl:List[EmployeeSchedule]):
        __listEmployee = Employee(self, __employeeId, __nameEmployee,  __salary, __role, __payRoll,
            __ranking, __listRanking, __scheduleEmpl, __listScheduleEmpl)
        self.__listEmployee.append(__listEmployee)

# End Methods


# gym1 = Gym(3453, 'Big Boys', 'Malabar', '3189086655', Campus)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'El nit del gym es {gym1.getNit()}\n'
#         f'El nombre del Gym es {gym1.getName()}\n'
#         f'La direccion del Gym es {gym1.getAddress()}\n'
#         f'El telefono del Gym es {gym1.getPhone()}\n'
#         f'La sede del Gym es {gym1.getCampus()}')
