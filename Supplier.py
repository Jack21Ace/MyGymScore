# Creación de la Clase Supplier : Proveedor
class Supplier:
    def __init__(self, __nit:int, __name:str, __phone:str, __emailAddress:str):
        self.nit = __nit
        self.name = __name
        self.phone = __phone
        self.emailAddress = __emailAddress

# getter && setter STARTS
    # Getter para nit
    def getNit(self):
        return self.nit

    # Getter && Setter para name
    def getName(self):
        return self.name

    def setName(self, __name):
        self.name = __name

    # Getter && Setter para phone
    def getPhone(self):
        return self.phone

    def setPhone(self, __phone):
        self.phone = __phone

    # Getter && Setter para emailAddress
    def getEmailAddress(self):
        return self.emailAddress

    def setEmailAddress(self, __emailAddress):
        self.emailAddress = __emailAddress
# getter && setter ENDS

# supplier1 = Supplier(8525649, 'Global Sport Ltda', '(606)886-4894', 'example@example.com')
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"Nuestro proveedor para maquinaria  es {supplier1.getName()}\n" +
# f"Su numero de contacto es {supplier1.getPhone()} \n" +
# f"Su Correo electronico es {supplier1.getEmailAddress()} \n" +
# f"Y su Nit es {supplier1.getNit()}")