# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:12:48 2021

@author: Juan Camilo
"""

from Enums import Type
import Supplier

#Creación de la clase item
class Item:
    # Declaración del constructor
    def __init__(self, __itemId:int, __name:str, __amount:int, __available:bool, __description:str, __type:Type, __supplier:Supplier):
        self.itemId = __itemId
        self.name = __name
        self.amount = __amount
        self.available = __available
        self.description = __description
        self.type = __type
        self.supplier = __supplier

# START METHODS
    # Getter para itemId
    def getItemId(self):
        return self.itemId

    # Getter && Setter para name
    def getName(self):
        return self.name

    def setName(self, __name):
        self.name = __name

    # Getter && Setter para amount
    def getAmount(self):
        return self.amount

    def setAmount(self, __amount):
        self.amount = __amount

    # Getter && Setter para available
    def getAvailable(self):
        return self.available

    def setAvailable(self, __available):
        self.available = __available

    # Getter && Setter para description
    def getDescription(self):
        return self.description

    def setDescription(self, __description):
        self.description = __description

    # Getter && Setter para type
    def getType (self):
        return self.type

    def setType(self, __type):
        self.type = __type

    # Getter && Setter para type
    def getSupplier (self):
        return self.Supplier

    def setSupplier(self, __supplier):
        self.supplier = __supplier
# ENDS METHODS

# instancia del Obj Item
# item1 = Item(122324, 'Colchoneta', 23, True, 'Ejercicios ABS', Type.STOOL, Supplier)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'La identificación del item es: {item1.getItemId()}\n'
#         f'El elemento es: {item1.getName()}\n'
#         f'La cantidad actual: {item1.getAmount()}\n'
#         f'Disponibilidad: {item1.getAvailable()}\n'
#         f'Descripcion: {item1.getDescription()}')
