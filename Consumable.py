from Enums import Conditioning, ConsumableType
from Product import Product

class Consumable(Product):
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