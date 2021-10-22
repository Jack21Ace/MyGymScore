from typing import Any, List

import User
import Supplier


class Campus(object):

    def __init__(self, __campusNit: int, __campusName: str, __campusPhone: str,
                __campusAddreess: str, __sizeParking: int, __technicalService: bool):
        self.__campusNit = __campusNit
        self.__campusName = __campusName
        self.__campusPhone = __campusPhone
        self.__campusAddreess = __campusAddreess
        self.__sizeParking = __sizeParking
        self.__inventario:Any =  List[Any()] # Composición Item
        self.__technicalService = __technicalService
        self.__bill:Any = List[Any()] # Composición
        self.__supplier:Supplier = List[Supplier()] # Composición
        self.__userList:User = List[User()] # Composición

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

    # getter && setter para SizeParking
    def getSizeParking(self):
        return self.__sizeParking

    def setSizeParking(self, __sizeParking:int):
        self.__sizeParking = __sizeParking

    # getter && setter para Inventario
    def getInventario(self):
        return self.__inventario

    def setInventario(self, __inventario:List[Any()]):
        self.__inventario = __inventario

    # getter && setter para technicalService
    def getTechnicalService(self):
        return self.__technicalService

    def setTechnicalService(self, __technicalService:bool):
        self.__technicalService = __technicalService

    # getter && setter para Bill
    def getBill(self):
        return self.__bill

    def setBill(self, __bill:List[Any()]):
        self.__bill = __bill

    # getter && setter para Supplier
    def getSupplier(self):
        return self.__supplier

    def setSupplier(self, __supplier:List[Supplier()]):
        self.__supplier = __supplier

    # getter && setter para userList
    def getUserList(self):
        return self.__userList

    def setUserList(self, __userList:List[Any]):
        self.__userList = __userList

    # Mejor forma para imprimir la información almacenada
    def __str__(self):
        pass