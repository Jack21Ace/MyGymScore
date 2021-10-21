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
    def __init__(self, __nameAccessory:str, __accessoryType:AccessoryType):
        self.nameAccessory = __nameAccessory
        self.accessoryType = __accessoryType

# START METHODS
    # Getter && Setter para nameAccessory
    def getNameAccessory(self):
        return self.nameAccessory
    
    def setNameAccessory(self, __nameAccessory):
        self.nameAccessory = __nameAccessory

    # Getter && Setter AccessoryType
    def getAccessoryType(self):
        return self.accessoryType

    def setAccessoryType(self, __accessoryType):
        self.accessoryType = __accessoryType