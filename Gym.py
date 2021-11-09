from typing import List
from Campus import Campus
from Employee import Employee
from Item import Item
from Supplier import Supplier
from Bill import Bill
from Payroll import Payroll
from Enums import Ranking, Role
from EmployeeSchedule import EmployeeSchedule
from User import User


# Crear clase Gym
class Gym:

    # Constructor
    def __init__(self, __nit:int, __name:str, __address:str, __phone:str):

        # Datos de entrada
        self.__nit = __nit
        self.__name = __name
        self.__address = __address
        self.__phone = __phone
        self.__campus = Campus(976431258, "Iron GYM", "8845632", "Villamaria", True, 13, False, User) # Composicion de Campus
        self.__listCampus:List = []
        self.__employee = Employee(2375, 'Oscar Andres', '317 8613343', 250000, Role.ADMINISTRATOR, Ranking.DOS)    # Composicion de Empleado
        self.__listEmployee:List = []

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

    def setCampus(self, __campus:Campus):
        self.__campus = __campus

    # Getter and Setter para listCampus
    def getListCampus(self):
        return self.__listCampus

    def setListCampus(self, __listCampus:List[Campus]):
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

    def setEmployee(self, __employee:Employee):
        self.__employee = __employee


    # Getter and Setter para listEmployee
    def getListEmployee(self):
        return self.__listEmployee

    def setListEmployee(self, __listEmployee:List[Employee]):
        self.__listEmployee = __listEmployee


    # Metodo ADD para Employee
    def addEmployee(self, __employeeId:int, __nameEmployee:str,  __salary:float, __role:Role, __payRoll:Payroll, __ranking:List[Ranking], __listRanking:List[Ranking], __scheduleEmpl:EmployeeSchedule, __listScheduleEmpl:List[EmployeeSchedule]):
        self.__employee = Employee(self, __employeeId, __nameEmployee,  __salary, __role, __payRoll,__ranking, __listRanking, __scheduleEmpl, __listScheduleEmpl)
        self.__listEmployee.append(self.__employee)
        return self.__listEmployee
# End Methods

    def __str__(self):
        result = f"El Nit del Gym es: {str(self.__nit)}\nNombre del GYM: {str(self.__name)}\nDirección: {str(self.__address)}\nTelefono: {str(self.__phone)}\nNombre del empleado encargado: {str(self.__employee.getNameEmployee())}\nNombre del campus: {str(self.__campus.getCampusName())}"
        return result
