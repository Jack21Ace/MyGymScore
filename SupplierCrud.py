class Proveedor:
    def __init__(self, nit:int,nombre:str,telefono:str,correo:str):
        self.nit:int = nit
        self.nombre:str = nombre
        self.telefono:str = telefono
        self.correo:str = correo
    def __str__(self):
        return f"Nombre= {self.nombre},Telefono= {self.telefono},Correo= {self.correo}"
    def getNombre(self):
        return self.nombre
    def getTelefono(self):
        return self.telefono
    def getCorreo(self):
        return self.correo
    def setNombre(self,nombre):
        self.nombre = nombre
    def setTelefono(self,telefono):
        self.telefono = telefono
    def setCorreo(self,correo):
        self.correo = correo


