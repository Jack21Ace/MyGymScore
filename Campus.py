from typing import Any, List
from Enums import Eps, Rh, Gender, Purpose, Type
from datetime import date

import User
import Bill
import Item
import Supplier


class Campus:

    def __init__(self, __campusNit: int, __campusName: str, __campusPhone: str, __campusAddreess: str,  
    __parking:bool,__sizeParking: int,__technicalService: bool, __user:User):
        self.__campusNit = __campusNit
        self.__campusName = __campusName
        self.__campusPhone = __campusPhone
        self.__campusAddreess = __campusAddreess
        self.__parking = __parking
        self.__sizeParking = __sizeParking
        self.__item:Item =  Item(122324, 'Colchoneta', 23, True, 'Ejercicios ABS', Type.PAD, Supplier) # Composición Item
        self.__inventario:List[Item()] = []
        self.__technicalService = __technicalService
        self.__bill:Bill = Bill(987456213, 123456789, "Arturo", "3105487425", "kr 25 # 24-13", date(2021, 3, 13), Any, Any) # Composición
        self.__supplier:Supplier = Supplier(8525649, 'Global Sport Ltda', '(606)886-4894', 'example@example.com') # Composición
        self.__userList:User = __user

    # getter para CampusNit
    def getCampusNit(self):
        return self.__campusNit

    # getter && setter para CampusName
    def getCampusName(self):
        return self.__campusName

    def setCampusName(self, __campusName:str):
        self.__campusName = __campusName

    # getter && setter para CampusPhone
    def getCampusPhone(self):
        return self.__campusPhone

    def setCampusPhone(self, __campusPhone:str):
        self.__campusPhone = __campusPhone

    # getter && setter para CampusAddreess
    def getCampusAddreess(self):
        return self.__campusAddreess

    def setCampusAddreess(self, __campusAddreess:str):
        self.__campusAddreess = __campusAddreess

    # getter && setter para parking
    def getParking(self):
        return self.__parking

    def setGarking(self, __parking:str):
        self.__parking = __parking

    # getter && setter para SizeParking
    def getSizeParking(self):
        return self.__sizeParking

    def setSizeParking(self, __sizeParking:int):
        self.__sizeParking = __sizeParking

    # getter && setter para Inventario
    def getInventario(self):
        return self.__inventario

    def setInventario(self, __inventario):
        self.__inventario= __inventario
    # getter && setter para technicalService
    def getTechnicalService(self):
        return self.__technicalService

    def setTechnicalService(self, __technicalService:bool):
        self.__technicalService = __technicalService

    # getter && setter para Bill
    def getBill(self):
        return self.__bill

    def setBill(self, __bill):
        self.__bill = __bill

    # getter && setter para Supplier
    def getSupplier(self):
        return self.__supplier

    def setSupplier(self, __supplier):
        self.__supplier = __supplier

    # getter && setter para userList
    def getUserList(self):
        return self.__userList

    def setUserList(self, __userList:List[Any]):
        self.__userList = __userList

    # Mejor forma para imprimir la información almacenada
    def __str__(self):
        result = f"Nombre del gimnasio: "
        return result

campus = Campus(316495151, "Iron Gym", "3145887742", "Villamaria", False, 0, True, User)
print(campus.__str__())