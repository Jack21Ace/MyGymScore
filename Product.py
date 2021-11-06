from datetime import  date
from typing import List
from Supplier import Supplier

# Clase Product
class Product: 

    # Constructor
    def __init__(self, __productId:int, __productName:str, __price:float, __brand:str,
                __expiration:date, __available:bool, __suppliers:List[Supplier]):

        # Datos de entrada
        self.__productId = __productId
        self.__productName = __productName
        self.__price = __price
        self.__brand = __brand
        self.__expiration = __expiration
        self.__available = __available
        self.__suppliers:List[Supplier] = __suppliers

# STARTS Metodos
    # Getter para productId
    def getProductId(self):
        return self.__productId 

    # Getter && Setter para product name
    def getProductName(self):
        return self.__productName

    def setProductName(self, __productName:str):
        self.__productName = __productName

    # Getter && Setter para price
    def getPrice(self):
        return self.__price

    def setPrice(self, __price:float): 
        self.__price = __price

    # Getter && Setter para brand
    def getBrand(self):
        return self.__brand

    def setBrand(self, __brand:str):
        self.__brand = __brand

    # Getter && Setter para expiration
    def getExpiration(self):
        return self.__expiration

    def setExpiration(self, __expiration:date):
        self.__expiration = __expiration

    # Getter && Setter para Available
    def getAvailable(self):
        return self.__available

    def setAvailable(self, __available:bool):
        self.__available = __available

    # Getter and Setter para supplier
    def getSuppliers(self):
        return self.__suppliers

    def setSuppliers(self, __suppliers:List[Supplier]):
        self.__suppliers = __suppliers


    def __str__(self) -> str:# PRODUCT 
        result = f"Nombre del producto: {str(self.__productName)}\nValor: {(self.__price):.3f}\nMarca: {str(self.__brand)}\nDisponibilidad: {str(self.__available)}\nProveedor: {str(self.__suppliers)}"
        return result
