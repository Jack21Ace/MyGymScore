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
    
    def getItemId(self):
        return self.itemId
    def getName(self):
        return self.name
    def setName(self, __name):
        self.name = __name
    def getAmount(self):
        return self.amount
    def setAmount(self, __amount):
        self.amount = __amount
    def getAvailable(self):
        return self.available
    def setAvailable(self, __available):
        self.available = __available
    def getDescription(self):
        return self.description
    def setDescription(self, __description):
        self.description = __description
    def getType (self):
        return self.type
    def setType(self, __type):
        self.type = __type
    def getSupplier (self):
        return self.supplier
    def setSupplier(self, __supplier):
        self.supplier = __supplier
    
item1 = Item(122324, 'Colchoneta', 23, True, 'Ejercicios ABS', Type.STOOL, Supplier) 

#print(f'La identificación del item es {item1.getItemId()}\nEl nombre es {item1.getName()}\nLa cantidad actual {item1.getAmount()}\nDisponibilidad {item1.getAvailable()}\nDescripcion {item1.getDescription()}\nEl tipo {item1.getType()}\n{item1.getSupplier()}')
print(f'La identificación del item es: {item1.getItemId()}\nEl elemento es: {item1.getName()}\nLa cantidad actual: {item1.getAmount()}\nDisponibilidad: {item1.getAvailable()}\nDescripcion: {item1.getDescription()}')
