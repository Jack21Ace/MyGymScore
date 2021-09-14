#Creación de la clase patology
class Patology:
    # Declaración del constructor
    def __init__(self, __name:str, __code:str):

        self.name = __name
        self.code = __code

    def getName(self):
        return self.name

    def setName(self, __name):
        self.name = __name

    def getCode(self):
        return self.code

    def setCode(self, __code):
        self.code = __code

# patology1 = Patology('Artritis', 'ABC012')
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'Sufre usted de: {patology1.getName()}, {patology1.getCode()}')

