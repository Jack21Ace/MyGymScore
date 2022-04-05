from Enums import UpperBody, LowerBody, Conditioning
class BodyZone:
    # Constructor
    def __init__(self, _upperBody:UpperBody, _lowerBody:LowerBody, _conditioning:Conditioning):

        # Datos de Entrada
        self._upperBody = _upperBody
        self._lowerBody = _lowerBody
        self._conditioning = _conditioning