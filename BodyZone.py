from Enums import UpperBody, LowerBody, Conditioning

# Creacion clase BodyZone
class BodyZone:

    # Constructor
    def __init__(self, __upperBody:UpperBody, __lowerBody:LowerBody, __conditioning:Conditioning):

        # Datos de Entrada
        self.upperBody = __upperBody
        self.lowerBody = __lowerBody
        self.conditioning = __conditioning

 # Metodos Getter and Setter

    # Getter && Setter Para UpperBody
    def getUpperBody(self):
        return self.upperBody

    def setUpperBody(self, __upperBody):
        self.upperBody = __upperBody

    # Getter && Setter Para LowerBody
    def getLowerBody(self):
        return self.lowerBody

    def setLowerBody(self, __lowerBody):
        self.lowerBody = __lowerBody

    # Getter && Setter Para Conditioning
    def getConditioning(self):
        return self.conditioning

    def setConditioning(self, __conditioning):
        self.conditioning = __conditioning

# Ejemplo

# bodyzone1 = BodyZone(UpperBody.ABDOMEN, LowerBody.QUADRICEPS_FEMORIS, Conditioning.RUN)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'El ejecicio de la zona superior es: {bodyzone1.getUpperBody()}\n'
#         f'El ejecicio de la zona baja es: {bodyzone1.getLowerBody()}\n'
#         f'El ejecicio de acondicionamiento es: {bodyzone1.getConditioning()}')


