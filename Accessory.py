# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:48:02 2021

@author: Juan Camilo
"""
from Enums import AccessoryType
from Product import Product
from Supplier import Supplier
from datetime import time
from typing import List
#Creación de la clase Accessory
class Accessory(Product):
    # Declaración del constructor
    def __init__(self, __accessoryType:AccessoryType, __productId:int, __productName:str, __price:float, __brand:str,
                __expiration:time, __available:bool, __suppliers:List[Supplier]):
        self.__accessoryType = __accessoryType

        Product.__init__(self, __productId, __productName, __price, __brand,
                __expiration, __available, __suppliers)

# START METHODS
    # Getter && Setter para nameAccessory
    def getNameAccessory(self):
        return self.__nameAccessory
    
    def setNameAccessory(self, __nameAccessory:str):
        self.__nameAccessory = __nameAccessory

    # Getter && Setter AccessoryType
    def getAccessoryType(self):
        return self.__accessoryType

    def setAccessoryType(self, __accessoryType:AccessoryType):
        self.__accessoryType = __accessoryType


