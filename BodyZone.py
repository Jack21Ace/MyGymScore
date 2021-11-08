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
    
    def __str__(self):
        result = f"Las rutinas se pueden dividir entre:\n {str(self.__conditioning.value)} como acondicionamiento fisico\n {str(self.__lowerBody.value)} para la zona inferior del cuerpo\n {str(self.__upperBody.value)} para la zona del tronco superior"
        return result
 


