from Enums import Type
from typing import Any, List, Mapping
from BodyZone import BodyZone
from DetailBill import DetailBill
from Employee import Employee
from Routine import Routine
from User import User
from Supplier import Supplier
from Item import Item

class Campus:

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

        self.__item = Item(122324, 'Colchoneta', 23, True, 'Ejercicios ABS', Type.PAD)   # Composición Item
        self.__inventario:List[self.__item] =  []

        self.__bill:List = []

        self.__supplier = Supplier(8525649, 'Global Sport Ltda', '(606)886-4894', 'example@example.com')  #  Composición Supplier
        self.__listSupplier:List[self.__supplier] = []

        self.__user = __user  # Agregacion
        self.__userList:List[User()] = []

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
    def getParking(self):
        return self.__parking

    def setParking(self, __parking:bool):
        self.__parking = __parking

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

    def setInventario(self, __inventario:List):
        self.__inventario = __inventario


    # # getter && setter para Bill
    # def getBill(self):
    #     return self.__bill

    # def setBill(self, __bill:List):
    #     self.__bill = __bill


    # getter && setter para Supplier
    def getSupplier(self):
        return self.__supplier

    def setSupplier(self, __supplier:Supplier):
        self.__supplier = __supplier


    # getter && setter para listSupplier
    def getlistSupplier(self):
        return self.__listSupplier

    def setlistSupplier(self, __listSupplier:List):
        self.__listSupplier = __listSupplier


    # getter && setter para user
    def getUser(self):
        return self.__user

    # getter && setter para userList
    def getUserList(self):
        return self.__userList

    def setUserList(self, __userList:List):
        self.__userList = __userList


    # Mejor forma para imprimir la información almacenada
    def __str__(self):
        result = f"Nombre del Gimnasio: {str(self.__campusName)}\nNit: {str(self.__campusNit)}\nTelefono: {str(self.__campusPhone)}\nNos encontramos en: {str(self.__campusAddreess)}\nTiene zona de parking?: {str(self.__parking)} - Espacios {str(self.__sizeParking)}\nServicio tecnico: {str(self.__technicalService)}\nEl nombre del  item es: {str(self.__item.getName())}\nEl nombre del proveedor es: {str(self.__supplier.getName())}"
        return result
