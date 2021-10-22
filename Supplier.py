class Supplier(object):
    def __init__(self, __nit:int, __name:str, __phone:str, __emailAddress:str):
        self.__nit = __nit
        self.__name = __name
        self.__phone = __phone
        self.__emailAddress = __emailAddress

# getter && setter STARTS
    # Getter para nit
    def getNit(self):
        return self.__nit

    # Getter && Setter para name
    def getName(self):
        return self.__name

    def setName(self, __name:str):
        self.__name = __name

    # Getter && Setter para phone
    def getPhone(self):
        return self.__phone

    def setPhone(self, __phone:str):
        self.__phone = __phone

    # Getter && Setter para emailAddress
    def getEmailAddress(self):
        return self.__emailAddress

    def setEmailAddress(self, __emailAddress:str):
        self.__emailAddress = __emailAddress
# getter && setter ENDS

    # Mejor forma para imprimir la información almacenada
    def __str__(self):
        pass

# supplier1 = Supplier(8525649, 'Global Sport Ltda', '(606)886-4894', 'example@example.com')
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"Nuestro proveedor para maquinaria  es {supplier1.getName()}\n" +
# f"Su numero de contacto es {supplier1.getPhone()} \n" +
# f"Su Correo electronico es {supplier1.getEmailAddress()} \n" +
# f"Y su Nit es {supplier1.getNit()}")