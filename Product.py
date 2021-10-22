from datetime import  datetime
from typing import List
from Supplier import Supplier

# Clase Product

#class Product(Accesory, Consumable) :
class Product : 

    # Constructor
    def __init__(self, __productId:int, __productName:str, __price:float, __brand:str, 
                __expiration:datetime, __available:bool, __supplier:Supplier, __listSupplier:List[Supplier]):

        # Datos de entrada
        self.__productId = __productId
        self.__productName = __productName
        self.__price = __price
        self.__brand = __brand
        self.__expiration = __expiration
        self.__available = __available

        self.__supplier = __supplier
        self.__listSupplier = __listSupplier
        self.__listSupplier:List[Supplier] = []

# STARTS Metodos
    # Getter para productId
    def getProductId(self):
        return self.__productId 


    # Getter && Setter para product name
    def getProductName(self):
        return self.__productName

    def setProductName(self, __productName):
        self.__productName = __productName


    # Getter && Setter para price
    def getPrice(self):
        return self.__price

    def setPrice(self, __price):
        self.__price = __price


    # Getter && Setter para brand
    def getBrand(self):
        return self.__brand

    def setBrand(self, __brand):
        self.__brand = __brand


    # Getter && Setter para expiration
    def getExpiration(self):
        return self.__expiration

    def setExpiration(self, __expiration):
        self.__expiration = __expiration


    # Getter && Setter para Available
    def getAvailable(self):
        return self.__available

    def setAvailable(self, __available):
        self.__available = __available

  
    # Getter and Setter para supplier
    def getSupplier(self):
        return self.__supplier
    
    def setSupplier(self, __supplier):
        self.__supplier = __supplier


    # Getter and Setter para listSupplier
    def getListSupplier(self):
        return self.__listSupplier
    
    def setListSupplier(self, __listSupplier):
        self.__listSupplier = __listSupplier



# Instanciop de la calse Product
# product1 = Product(5677, Supplier, 40950, ProductType.SUPPLEMENTS, 'ActivoFUSHION', date(2021, 11, 2))
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'El ID del Producto es: {product1.getProductId()}\n'
#         f'El nombre del Proveedor es  {product1.getSupplier()}\n'
#         f'El precio del producto es {product1.getPrice()}\n'
#         f'El tipo del producto es {product1.getType()}\n'
#         f'La marca del producto es {product1.getBrand()}\n'
#         f'La fecha de expiracion del producto es {product1.getExpiration()}')
