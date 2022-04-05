# from typing import Any, List, Mapping
# from BodyZone import BodyZone
# from DetailBill import DetailBill
# from Employee import Employee
# from Routine import Routine
from Enums import Type
from User import User
from SupplierCrud import Proveedor

# Crear clase Gym
class Campus:
    # Constructor
    def __init__(self, __campusNit: int, __campusName: str, __campusPhone: str,
                __campusAddreess: str, __parking:bool, __sizeParking: int, __technicalService: bool, __user:User):
        # Datos de entrada
        self.__campusNit = __campusNit
        self.__campusName = __campusName
        self.__campusPhone = __campusPhone
        self.__campusAddreess = __campusAddreess
        self.__parking = __parking
        self.__sizeParking = __sizeParking
        self.__technicalService = __technicalService
        self.__item = Proveedor(122324, 'Colchoneta', '6068848484', 'holi@example.com')   # Composición Item
       #self.__listCampus:List = []
       #self.__employee = Employee(2375, 'Oscar Andres', '317 8613343', 250000, Role.ADMINISTRATOR, Ranking.DOS)    # Composicion de Empleado
       #self.__listEmployee:List = []


    # Getter and Setter

    def __str__(self):
        return f"Nombre= {self.__campusName},Telefono= {self.__campusPhone},Dirección= {self.__campusAddreess}"

    def getCampusName(self):
        return self.__campusName
    def getCampusPhone(self):
        return self.__campusPhone
    def getCampusAddress(self):
        return self.__campusAddreess
    def setCampusName(self,__campusName):
        self.__campusName = __campusName
    def setCampusPhone(self,__campusPhone):
        self.__campusPhone = __campusPhone
    def setCampusAddreess(self,__campusAddreess):
        self.__campusAddreess = __campusAddreess