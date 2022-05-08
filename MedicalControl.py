from datetime import date
from typing import Any

class MedicalControl:
    # Declaración del constructor o Inicializador de tipo objeto
    def __init__(self, medicEmploName:str, diagnosis:str, treatment:str, suggestions:str, medicalDate:date,
    evolutionaryLevel:float, patologies:list):
    # patología es agregación no es obligación
    # composición depende si o si de la otra clase

    # Datos de entrada
        self._medicEmploName = medicEmploName
        self._diagnosis = diagnosis ##select, ctrl + d,++ flecha der, ctrl + flecha izquierda - con el fin de privar el codigo
        self._treatment = treatment
        self._suggestions = suggestions
        self._medicalDate = medicalDate
        self._evolutionaryLevel = evolutionaryLevel
        self._patologies:list = patologies

# START METHODS
    # Getter && Setter para medicEmploName
    def getMedicEmploName(self):
        return self._medicEmploName

    def setMedicEmploName(self, medicEmploName:str):
        self._medicEmploName = medicEmploName

    # Getter && Setter para diagnosis
    def getDiagnosis(self):
        return self._diagnosis

    def setDiagnosis(self, diagnosis:str):
        self._diagnosis = diagnosis

    # Getter && Setter para treatment
    def getTreatment(self):
        return self._treatment

    def setTreatment(self, treatment:str):
        self._treatment = treatment

    # Getter && Setter para suggestions
    def getSuggestions(self):
        return self._suggestions

    def setSuggestions(self, suggestions):
        self._suggestions = suggestions

    # Getter && Setter para medicalDate
    def getMedicalDate(self):
        return self._medicalDate

    def setMedicalDate(self, medicalDate:date):
        self._medicalDate = medicalDate

    # Getter && Setter para evolutionaryLevel
    def getEvolutionaryLevel(self):
        return self._evolutionaryLevel

    def setEvolutionaryLevel(self, evolutionaryLevel:float):
        self._evolutionaryLevel = evolutionaryLevel

    # Getter && Setter para patologies
    def getPatologies(self):
        return self._patologies

    def setPatologies(self, patologies:list):
        self._patologies = patologies

    def __str__(self):
        result = f"El medico que le atiende es: {str(self._medicEmploName)}\nDiagnostico Medico: {str(self._diagnosis)}\nTratamiento: {str(self._treatment)}\nSugerencia: {str(self._suggestions)}\nFecha de la Cita: {str(self._medicalDate)}\nNivel Evolutivo en el GYM: {str(self._evolutionaryLevel)}\nCodigo Patologia: {str(self._patologies)}"
        return result

obj_MC = MedicalControl("Dr. Rojas", "Paciente con fractura en muñeca derecha, reco: Terapia F", "Rutinas poco peso, fuertes repeticiones", "todos los días", date(2022, 5, 7), 0.0, ['A5248','A9634', 'R9865'])
print(obj_MC)