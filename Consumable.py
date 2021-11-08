from Enums import Conditioning, ConsumableType
from Product import Product

class Consumable(Product):
    def __init__(self, __consumableType:ConsumableType, __productId, 
        __productName, __price, __brand, __expiration, __available, __suppliers):
        self.__consumableType = __consumableType

        Product.__init__(self, __productId, __productName, __price, __brand,
                __expiration, __available, __suppliers)

    def getConsumableType(self):
        return self.__consumableType

    def setConsumableType(self, __consumableType:ConsumableType):
        self.__consumableType = __consumableType