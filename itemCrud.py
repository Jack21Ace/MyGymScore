from time import monotonic
from typing import Any
#from SupplierCrud import Proveedor


class Item:
    def __init__(self, iditem:int,nombre:str,monto:float,estado:bool,descripcion:str,tipo:type,proveedor:Any):
        self.iditem:int = iditem
        self.nombre:str = nombre
        self.monto:float = monto
        self.estado:bool = estado
        self.descripcion:str = descripcion 
        self.tipo:type = tipo
        self.proveedor = proveedor
    def __str__(self):
        return f"Nombre= {self.nombre},Monto= {self.monto}"
    def getNombre(self):
        return self.nombre
    def getMonto(self):
        return self.monto
    def setNombre(self,nombre):
        self.nombre = nombre
    def setMonto(self,monto):
        self.monto = monto
    def setEstado(self,estado):
        self.estado = estado
    def setDescripcion(self,descripcion):
        self.descripcion = descripcion
    def setTipo(self,tipo):
        self.tipo = tipo
    def setProveedor(self,proveedor):
        self.proveedor = proveedor