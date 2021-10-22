from Enums import UpperBody, LowerBody, Conditioning

# Creacion clase BodyZone
class BodyZone:

    # Constructor
    def __init__(self, __upperBody:UpperBody, __lowerBody:LowerBody, __conditioning:Conditioning):

        # Datos de Entrada
        self.__upperBody = __upperBody
        self.__lowerBody = __lowerBody
        self.__conditioning = __conditioning

 # Metodos Getter and Setter

    # Getter && Setter Para UpperBody
    def getUpperBody(self):
        return self.__upperBody

    def setUpperBody(self, __upperBody:UpperBody):
        self.__upperBody = __upperBody

    # Getter && Setter Para LowerBody
    def getLowerBody(self):
        return self.__lowerBody

    def setLowerBody(self, __lowerBody:LowerBody):
        self.__lowerBody = __lowerBody

    # Getter && Setter Para Conditioning
    def getConditioning(self):
        return self.__conditioning

    def setConditioning(self, __conditioning:Conditioning):
        self.__conditioning = __conditioning

# Ejemplo

# bodyzone1 = BodyZone(UpperBody.ABDOMEN, LowerBody.QUADRICEPS_FEMORIS, Conditioning.RUN)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'El ejecicio de la zona superior es: {bodyzone1.getUpperBody()}\n'
#         f'El ejecicio de la zona baja es: {bodyzone1.getLowerBody()}\n'
#         f'El ejecicio de acondicionamiento es: {bodyzone1.getConditioning()}')


