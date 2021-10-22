#Creación de la clase patology
class Patology(object): #Clase de tipo objeto
    # Declaración del constructor
    def __init__(self, __name:str, __code:str):

        self.__name = __name
        self.__code = __code
        pass

    def getName(self):
        return self.__name

    def setName(self, __name):
        self.__name = __name

    def getCode(self):
        return self.__code

    def setCode(self, __code):
        self.__code = __code

# patology1 = Patology('Artritis', 'ABC012')
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'Sufre usted de: {patology1.getName()}, {patology1.getCode()}')

