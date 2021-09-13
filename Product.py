from enum import Enum
from datetime import date
from Enums import ProductType
from typing import Any

# Clase Product
import Supplier
class Product :

    # Constructor
    def __init__(self, __productId:int, __supplier:Supplier, __price:float,
                __type:ProductType, __brand:str, __expiration:date):
        # Datos de entrada
        self.productId = __productId
        self.supplier = __supplier
        self.price = __price
        self.type = __type
        self.brand = __brand
        self.expiration = __expiration

# STARTS Metodos
    # Getter para productId
    def getProductId(self):
        return self.productId

    # Getter && Setter para supplier
    def getSupplier(self):
        return self.supplier

    def setSupplier(self, __supplier):
        self.supplier = __supplier

    # Getter && Setter para price
    def getPrice(self):
        return self.price

    def setPrice(self, __price):
        self.price = __price

    # Getter && Setter para type
    def getType(self):
        return self.type

    def setType(self, __type):
        self.type = __type

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


# Instanciop de la calse Product
product1 = Product(5677, Supplier, 40950, ProductType.SUPPLEMENTS, 'ActivoFUSHION', date(2021, 11, 2))
print("==========//==========//==========//==========//==========//==========//==========")
print(f'El ID del Producto es: {product1.getProductId()}\n'
        f'El nombre del Proveedor es  {product1.getSupplier()}\n'
        f'El precio del producto es {product1.getPrice()}\n'
        f'El tipo del producto es {product1.getType()}\n'
        f'La marca del producto es {product1.getBrand()}\n'
        f'La fecha de expiracion del producto es {product1.getExpiration()}')

# Se remueve el atributo name
# Preguntar por la lista supilier de la clase supilier