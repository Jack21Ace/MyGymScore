from Patology import Patology
from datetime import date, time
from typing import Any, List

class MedicalControl:
    # Declaración del constructor o Inicializador de tipo objeto
    def __init__(self, __medicEmploName:str, __diagnosis:str, __treatment:str, __suggestions:str, __medicalDate:date,
    __evolutionaryLevel:float, __patologies:List[Patology]):
    # patología es agregación no es obligación
    # composición depende si o si de la otra clase

    # Datos de entrada
        self.__medicEmploName = __medicEmploName
        self.__diagnosis = __diagnosis ##select, ctrl + d,++ flecha der, ctrl + flecha izquierda - con el fin de privar el codigo
        self.__treatment = __treatment
        self.__suggestions = __suggestions
        self.__medicalDate = __medicalDate
        self.__evolutionaryLevel = __evolutionaryLevel
        self.__patologies:List[Patology] = __patologies

# START METHODS
    # Getter && Setter para medicEmploName
    def getMedicEmploName(self):
        return self.__medicEmploName

    def setMedicEmploName(self, __medicEmploName:str):
        self.medicEmploName = __medicEmploName

    # Getter && Setter para diagnosis
    def getDiagnosis(self):
        return self.__diagnosis

    def setDiagnosis(self, __diagnosis:str):
        self.__diagnosis = __diagnosis

    # Getter && Setter para treatment
    def getTreatment(self):
        return self.__treatment

    def setTreatment(self, __treatment:str):
        self.__treatment = __treatment

    # Getter && Setter para suggestions
    def getSuggestions(self):
        return self.__suggestions

    def setSuggestions(self, __suggestions):
        self.__suggestions = __suggestions

    # Getter && Setter para __medicalDate
    def getMedicalDate(self):
        return self.__medicalDate

    def setMedicalDate(self, __medicalDate:date):
        self.__medicalDate = __medicalDate

    # Getter && Setter para __evolutionaryLevel
    def getEvolutionaryLevel(self):
        return self.__evolutionaryLevel

    def setEvolutionaryLevel(self, __evolutionaryLevel:float):
        self.__evolutionaryLevel = __evolutionaryLevel

    def addPatology(self, __name:str, __code:str):
        patology = Patology(self, __name, __code)
        self.__patologies.append(patology)

    # revisar GET
    def getPatology(code:int):
        pass

    def searchPatology(searchFor:List[Patology]):
        pass

    # Getter && Setter para patologies
    def getPatologies(self):
        return self.__patologies

    def setPatologies(self, __patologies:Patology):
        self.__patologies = __patologies

    def __str__(self):
        result = f"El medico que le atiende es: {str(self.__medicEmploName)}\nDiagnostico Medico: {str(self.__diagnosis)}\nTratamiento: {str(self.__treatment)}\nSugerencia: {str(self.__suggestions)}\nFecha de la Cita: {str(self.__medicalDate)}\nNivel Evolutivo en el GYM: {str(self.__evolutionaryLevel)}\nCodigo Patologia: {str(self.__patologies)}"
        return result



