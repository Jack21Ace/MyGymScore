from typing import Any, List, Mapping
from Bill import Bill
from BodyZone import BodyZone
from DetailBill import DetailBill
from Employee import Employee
from Gym import Gym
from Routine import Routine

from User import User
from Supplier import Supplier
from Item import Item
 
class Campus:

    def __init__(self, __campusNit: int, __campusName: str, __campusPhone: str,
                __campusAddreess: str, __sizeParking: int, __technicalService: bool, __user:User): 

        # Datos de entrada
        self.__campusNit = __campusNit
        self.__campusName = __campusName
        self.__campusPhone = __campusPhone
        self.__campusAddreess = __campusAddreess
        self.__sizeParking = __sizeParking
        self.__technicalService = __technicalService
        self.__item = Item()      # Composición Item
        self.__inventario:List[Item] =  [] 

        self.__bill:Any = List[Any()] # Composición Bill

        self.__supplier = Supplier()  #  Composición Supplier 
        self.__listSupplier:List[Supplier] = [] 

        self.__user = __user  # Agregacion 
        self.__userList:List[User] = [] 

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

    # getter && setter para technicalService
    def getTechnicalService(self):
        return self.__technicalService

    def setTechnicalService(self, __technicalService:bool):
        self.__technicalService = __technicalService

    # getter && setter para Item
    def getItem(self):
        return self.__item
    
    def setItem(self, __item:Item):
        self.__item = __item

    # getter && setter para Inventario
    def getInventario(self):
        return self.__inventario

    def setInventario(self, __inventario:List[Item]):
        self.__inventario = __inventario


    # getter && setter para Bill
    def getBill(self):
        return self.__bill

    def setBill(self, __bill:List[Any()]):
        self.__bill = __bill


    # getter && setter para Supplier
    def getSupplier(self):
        return self.__supplier

    def setSupplier(self, __supplier:Supplier):
        self.__supplier = __supplier

    # getter && setter para listSupplier
    def getlistSupplier(self):
        return self.__listSupplier

    def setlistSupplier(self, __listSupplier:List[Supplier]):
        self.__listSupplier = __listSupplier


    # getter && setter para user
    def getUser(self):
        return self.__user
    
    # getter && setter para userList
    def getUserList(self):
        return self.__userList

    def setUserList(self, __userList:List[User]):
        self.__userList = __userList


    # Mejor forma para imprimir la información almacenada
    def __str__(self):
        pass

