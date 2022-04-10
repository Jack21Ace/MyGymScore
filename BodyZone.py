<<<<<<< Updated upstream
from Enums import UpperBody, LowerBody, Conditioning
class BodyZone:
    # Constructor
    def __init__(self, _upperBody:UpperBody, _lowerBody:LowerBody, _conditioning:Conditioning):

        # Datos de Entrada
        self._upperBody = _upperBody
        self._lowerBody = _lowerBody
        self._conditioning = _conditioning
=======
from Enums import UpperBody, LowerBody, Conditioning

# Creacion clase BodyZone
class BodyZone:

    # Constructor
    def __init__(self, __upperBody:UpperBody, __lowerBody:LowerBody, __conditioning:Conditioning):

        # Datos de Entrada
        self.upperBody = __upperBody
        self.lowerBody = __lowerBody
        self.conditioning = __conditioning

    # Metodos
    def getUpperBody(self):
        return self.upperBody

    def getLowerBody(self):
        return self.lowerBody

    def getConditioning(self):
        return self.conditioning

    def setUpperBody(self, __upperBody):
        self.upperBody = __upperBody

    def setLowerBody(self, __lowerBody):
        self.lowerBody = __lowerBody

    def setConditioning(self, __conditioning):
        self.conditioning = __conditioning

# Ejemplo

# bodyzone1 = BodyZone(UpperBody.ABDOMEN, LowerBody.QUADRICEPS_FEMORIS, Conditioning.RUN)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'El ejecicio de la zona superior es: {bodyzone1.getUpperBody()}\n'
#         f'El ejecicio de la zona baja es: {bodyzone1.getLowerBody()}\n'
#         f'El ejecicio de acondicionamiento es: {bodyzone1.getConditioning()}')


>>>>>>> Stashed changes
