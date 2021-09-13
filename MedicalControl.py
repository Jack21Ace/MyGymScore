from Patology import Patology
from datetime import date, time
from typing import Any

class MedicalControl:
    # Declaración del constructor
    def __init__(self, __medicId:int, __medicEmploName:str, __diagnosis:str, __treatment:str, __suggestions:str, __medicalDate:date, __medicalTime:date, __evolutionaryLevel:float, __patologies:Patology):

    # Datos de entrada

        self.medicId = __medicId
        self.medicEmploName = __medicEmploName
        self.diagnosis = __diagnosis
        self.treatment = __treatment
        self.suggestions = __suggestions
        self.medicalDate = __medicalDate
        self.evolutionaryLevel = __evolutionaryLevel
        self.patologies = __patologies
        self.medicalTime = __medicalTime

# START METHODS
    # Getter para medicId
    def getMedicId(self):
        return self.medicId

    # Getter && Setter para medicEmploName
    def getMedicEmploName(self):
        return self.medicEmploName

    def setMedicEmploName(self, __medicEmploName):
        self.medicEmploName = __medicEmploName

    # Getter && Setter para diagnosis
    def getDiagnosis(self):
        return self.diagnosis

    def setDiagnosis(self, __diagnosis):
        self.diagnosis = __diagnosis

    # Getter && Setter para treatment
    def getTreatment(self):
        return self.treatment

    def setTreatment(self, __treatment):
        self.treatment = __treatment

    # Getter && Setter para suggestions
    def getSuggestions(self):
        return self.suggestions

    def setSuggestions(self, __suggestions):
        self.suggestions = __suggestions

    # Getter && Setter para medicalDate
    def getMedicalDate(self):
        return self.medicalDate

    def setMedicalDate(self, __medicalDate):
        self.medicalDate = __medicalDate

    # Getter && Setter para evolutionaryLevel
    def getEvolutionaryLevel(self):
        return self.evolutionaryLevel

    def setEvolutionaryLevel(self, __evolutionaryLevel):
        self.evolutionaryLevel = __evolutionaryLevel

    # Getter && Setter para patologies
    def getPatologies(self):
        return self.patologies

    def setPatologies(self, __patologies):
        self.patologies = __patologies

    # Getter && Setter para medicalTime
    def getMedicalTime(self):
        return self.medicalTime

    def setMedicalTime(self, __medicalTime):
        self.medicalTime = __medicalTime

#
medicalControl1 = MedicalControl(1234, 'Alvaro','Desgarro Muscular','Analgesicos','Fisioterapia',date(2021, 9,28),time(13,30,5), 1.5, Patology)
print("==========//==========//==========//==========//==========//==========//==========")
print(f'Usted presenta {medicalControl1.getDiagnosis()}')



