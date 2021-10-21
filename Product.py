from enum import Enum
from datetime import date, datetime
from Enums import ProductType
from typing import List, Any
from Supplier import Supplier

# Clase Product

class Product :

    # Constructor
    def __init__(self, __productId:int, __productName:str, __price:float, __brand:str, __expiration:datetime, __available:bool, __supplier:List[Any]):
        # Datos de entrada
        self.productId = __productId
        self.productName = __productName
        self.price = __price
        self.brand = __brand
        self.expiration = __expiration
        self.available = __available
        self.supplier = __supplier

# STARTS Metodos
    # Getter para productId
    def getProductId(self):
        return self.productId 


    # Getter && Setter para product name
    def getProductName(self):
        return self.productName

    def setProductName(self, __productName):
        self.productName = __productName


    # Getter && Setter para price
    def getPrice(self):
        return self.price

    def setPrice(self, __price):
        self.price = __price


    # Getter && Setter para brand
    def getBrand(self):
        return self.brand

    def setBrand(self, __brand):
        self.brand = __brand


    # Getter && Setter para expiration
    def getExpiration(self):
        return self.expiration

    def setExpiration(self, __expiration):
        self.expiration = __expiration


    # Getter && Setter para Available
    def getAvailable(self):
        return self.available

    def setAvailable(self, __available):
        self.available = __available

  
    # Getter para supplier
    def getSupplier(self):
        return self.supplier




# La HERENCIA se pone en la clase HIja, en este caso se debe incorporar la clase Product en Accesory y Consumable asi:
#   class Accesory(Product):
#   class Consumable(Product):



# Instanciop de la calse Product
# product1 = Product(5677, Supplier, 40950, ProductType.SUPPLEMENTS, 'ActivoFUSHION', date(2021, 11, 2))
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'El ID del Producto es: {product1.getProductId()}\n'
#         f'El nombre del Proveedor es  {product1.getSupplier()}\n'
#         f'El precio del producto es {product1.getPrice()}\n'
#         f'El tipo del producto es {product1.getType()}\n'
#         f'La marca del producto es {product1.getBrand()}\n'
#         f'La fecha de expiracion del producto es {product1.getExpiration()}')
