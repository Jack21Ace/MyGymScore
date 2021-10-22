# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:47:16 2021

@author: Juan Camilo
"""

from Enums import Type
import Supplier

#Creación de la clase item
class Item:
    # Declaración del constructor
    def __init__(self, __itemId:int, __name:str, __amount:int, __available:bool, __description:str, __type:Type, __supplier:Supplier):
        self.__itemId = __itemId
        self.__name = __name
        self.__amount = __amount
        self.__available = __available
        self.__description = __description
        self.__type = __type
        self.__supplier = __supplier

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
        return self.__Supplier

    def setSupplier(self, __supplier:Supplier):
        self.__supplier = __supplier
# ENDS METHODS

# instancia del Obj Item
# item1 = Item(122324, 'Colchoneta', 23, True, 'Ejercicios ABS', Type.STOOL, Supplier)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'La identificación del item es: {item1.getItemId()}\n'
#         f'El elemento es: {item1.getName()}\n'
#         f'La cantidad actual: {item1.getAmount()}\n'
#         f'Disponibilidad: {item1.getAvailable()}\n'
#         f'Descripcion: {item1.getDescription()}')  