# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:48:02 2021

@author: Juan Camilo
"""

from Enums import AccesoryType
from Product import Product
#Creación de la clase Accessory
class Accessory(Product):
    # Declaración del constructor
    def __init__(self, __nameAccessory:str, __accessoryType:AccesoryType):
        self.__nameAccessory = __nameAccessory
        self.__accessoryType = __accessoryType

# START METHODS
    # Getter && Setter para nameAccessory
    def getNameAccessory(self):
        return self.__nameAccessory
    
    def setNameAccessory(self, __nameAccessory:str):
        self.__nameAccessory = __nameAccessory

    # Getter && Setter AccessoryType
    def getAccessoryType(self):
        return self.__accessoryType

    def setAccessoryType(self, __accessoryType:AccesoryType):
        self.__accessoryType = __accessoryType