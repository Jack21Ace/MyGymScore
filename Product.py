from enum import Enum
from datetime import date
from Enums import ProductType
from typing import Any

# Clases Pendientes
#import Supplier

# Clase Product
class Product :

    # Constructor 
    def __init__(self, __productId:int, __supplier:Any, __price:float, 
                __type:ProductType, __brand:str, __expiration:date):
                
        # Datos de entrada 
        self.productId = __productId
        self.supplier = __supplier
        self.price = __price
        self.type = __type
        self.brand = __brand
        self.expiration = __expiration

    # Metodos
    
    # get
    def getProductId(self):
        return self.productId

    def getSupplier(self):
        return self.supplier
    
    def getPrice(self):
        return self.price
    
    def getType(self):
        return self.type
    
    def getBrand(self):
        return self.brand
    
    def getExpiration(self):
        return self.expiration

    # set

    def setSupplier(self, __supplier):
        self.supplier = __supplier
    
    def setPrice(self, __price):
        self.price = __price
    
    def setType(self, __type):
        self.type = __type
    
    def setBrand(self, __brand):
        self.brand = __brand
    
    def setExpiration(self, __expiration):
        self.expiration = __expiration


# EJEMPLO 

product1 = Product(5677, 'Tipo Supplier', 40950, ProductType.SUPPLEMENTS, 'ActivoFUSHION', date(2021, 11, 2))

print(f'El ID del Producto es: {product1.getProductId()}\n') 
print(f'El nombre del Proveedor es  {product1.getSupplier()}\n')
print(f'El precio del producto es {product1.getPrice()}\n')
print(f'El tipo del producto es {product1.getType()}\n')
print(f'La marca del producto es {product1.getBrand()}\n')
print(f'La fecha de expiracion del producto es {product1.getExpiration()}\n')

 

# Se remueve el atributo name
        
# Preguntar por la lista supilier de la clase supilier 