# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:47:16 2021

@author: Juan Camilo
"""

from Enums import Type
from Supplier import Supplier

#Creación de la clase item
class Item:
    # Declaración del constructor
    def __init__(self, __itemId:int, __name:str, __amount:int, __available:bool, __description:str, __type:Type):
        self.__itemId = __itemId
        self.__name = __name
        self.__amount = __amount
        self.__available = __available
        self.__description = __description
        self.__type = __type
        self.__supplier = Supplier(8525649, 'Global Sport Ltda', '(606)886-4894', 'example@example.com')

# START METHODS
    # Getter para itemId
    def getItemId(self):
        return self.__itemId

    # Getter && Setter para name
    def getName(self):
        return self.__name

    def setName(self, __name:str):
        self.__name = __name

    # Getter && Setter para amount
    def getAmount(self):
        return self.__amount

    def setAmount(self, __amount:int):
        self.__amount = __amount

    # Getter && Setter para available
    def getAvailable(self):
        return self.__available

    def setAvailable(self, __available:bool):
        self.__available = __available

    # Getter && Setter para description
    def getDescription(self):
        return self.__description

    def setDescription(self, __description:str):
        self.__description = __description

    # Getter && Setter para type
    def getType (self):
        return self.__type

    def setType(self, __type:Type):
        self.__type = __type

    # Getter && Setter para type
    def getSupplier (self):
        return self.__supplier

    def setSupplier(self, __supplier:Supplier):
        self.__supplier = __supplier
# ENDS METHODS
    def __str__(self):
        result = f"El elemnto es: {str(self.__name)}\nSu codigo es: {str(self.__itemId)}\nEn inventario tenemos: {str(self.__amount)}\nDisponibles: {str(self.__available)}\nDescripción: {str(self.__description)}\nTipo: {str(self.__type.value)}\nProveedor: {str(self.__supplier.getName())}"
        return result