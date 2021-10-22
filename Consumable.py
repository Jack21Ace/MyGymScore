from Enums import Conditioning, ConsumableType

class Consumable(object):
    __nameConsumable: str = ""
    __consumableType:ConsumableType = None

    def getNameConsumable(self):
        return self.__nameConsumable

    def setNameConsumable(self, __nameConsumable:str):
        self.__nameConsumable = __nameConsumable

    def getConsumableType(self):
        return self.__consumableType

    def setConsumableType(self, __consumableType:ConsumableType):
        self.__consumableType = __consumableType