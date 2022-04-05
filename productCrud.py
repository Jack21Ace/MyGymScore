from enum import Enum
from datetime import date, datetime
#from Enums import ProductType
from typing import Any
#from SupplierCrud import Proveedor



class Product :
    def __init__(self, productId:int,productNombre:str,precio:float,marca:str,vencimiento:datetime,disponible:bool,proveedor:Any):
        self.productId:int= productId
        self.productNombre:str = productNombre
        self.precio:float = precio
        self.marca:str = marca
        self.vencimiento:datetime = vencimiento
        self.disponible:bool = disponible
        self.proveedor = proveedor


    def __str__(self):
        return f"= {str(self.productNombre)},precio= {str(self.precio)}"
    def getProductNombre(self):
        return self.productNombre
    def getPrecio(self):
        return self.precio
    def setProductNombre(self,productNombre):
        self.productNombre = productNombre
    def setPrecio(self,precio):
        self.precio = precio
    def setMarca(self,marca):
        self.marca= marca
    def setVencimiento(self,vencimiento):
        self.vencimiento= vencimiento
    def setDisponible(self,disponible):
        self.disponible= disponible
    def setProveedor(self,proveedor):
        self.proveedor= proveedor

