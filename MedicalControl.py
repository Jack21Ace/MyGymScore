from datetime import date
from typing import Any

class MedicalControl:
    # Declaracion de Variables
    # cola vacia
    emptyQueue:list = []
    # head
    head:int = 0

    # Declaración del constructor o Inicializador de tipo objeto
    def __init__(self, medicEmploName:str, diagnosis:str, treatment:str, suggestions:str, medicalDate:date,
    evolutionaryLevel:float, patologies:list):
    # patología es agregación no es obligación
    # composición depende si o si de la otra clase

    # Datos de entrada
        self._medicEmploName = medicEmploName
        self._diagnosis = diagnosis
        self._treatment = treatment
        self._suggestions = suggestions
        self._medicalDate = medicalDate
        self._evolutionaryLevel = evolutionaryLevel
        self._patologies:list = patologies
        self.size = 7

# START METHODS
    # Getter && Setter para medicEmploName
    @property
    def medicEmploName(self):
        return self._medicEmploName

    @medicEmploName.setter
    def medicEmploName(self, medicEmploName:str):
        self._medicEmploName = medicEmploName

    @medicEmploName.deleter
    def medicEmploName(self):
        del self._medicEmploName

    # Getter && Setter para diagnosis
    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, diagnosis:str):
        self._diagnosis = diagnosis

    @diagnosis.deleter
    def diagnosis(self):
        del self._diagnosis

    # Getter && Setter para treatment
    @property
    def treatment(self):
        return self._treatment

    @treatment.setter
    def treatment(self, treatment:str):
        self._treatment = treatment

    @treatment.deleter
    def treatment(self):
        del self._treatment

    # Getter && Setter para suggestions
    @property
    def suggestions(self):
        return self._suggestions

    @suggestions.setter
    def suggestions(self, suggestions):
        self._suggestions = suggestions

    @suggestions.deleter
    def suggestions(self):
        del self._suggestions

    # Getter && Setter para medicalDate
    @property
    def medicalDate(self):
        return self._medicalDate

    @medicalDate.setter
    def medicalDate(self, medicalDate:date):
        self._medicalDate = medicalDate

    @medicalDate.deleter
    def medicalDate(self):
        del self._medicalDate

    # Getter && Setter para evolutionaryLevel
    @property
    def evolutionaryLevel(self):
        return self._evolutionaryLevel

    @evolutionaryLevel.setter
    def evolutionaryLevel(self, evolutionaryLevel:float):
        self._evolutionaryLevel = evolutionaryLevel

    @evolutionaryLevel.deleter
    def evolutionaryLevel(self):
        del self._evolutionaryLevel

    # Getter && Setter para patologies
    @property
    def patologies(self):
        return self._patologies

    @patologies.setter
    def setPatologies(self, patologies:list):
        self._patologies = patologies

    @patologies.deleter
    def patologies(self):
        del self._patologies

    def __str__(self):
        return f"El medico que le atiende es: {str(self.medicEmploName)}\nDiagnostico Medico: {str(self.diagnosis)}\nTratamiento: {str(self.treatment)}\nSugerencia: {str(self.suggestions)}\nFecha de la Cita: {str(self.medicalDate)}\nNivel Evolutivo en el GYM: {str(self.evolutionaryLevel)}\nCodigo Patologia: {str(self.patologies)}"

#     def enqueue(self, data):
#         if (len(self.queue) >= self.size):
#             print(f"Queue is Full!!!!")
#             result = list(map(lambda x:x, data))
#             print(result)
#         else:
#             input("Ingrese datos de la rutina a encolar")
#             medicEmploName = str(input("Medico quién atiende: "))
#             diagnosis = str(input("Diagnostico: "))
#             treatment = str(input("Tratamiento: "))
#             suggestions = str(input("Sugerencias: "))
#             medicalDate = str(input("Fecha cita: "))
#             evolutionaryLevel = float(input("Nivel evolutivo: "))
#             patologies = str(input("Patologia nueva: "))
#             self.e = MedicalControl(medicEmploName, diagnosis, treatment, suggestions, medicalDate, evolutionaryLevel, patologies)
#             self.queue[:0] = [self.e]
#             print(self.queue)

#     def dequeue(self):
#         if not self.queue:
#             print('Queue is Empty!!')
#         else:
#             self.head = self.queue[-1]
#             tem = self.queue[:-1]
#             self.queue = tem
#             print(f'Element removed: {self.head.medicalDate}\n{self.head}\n{self.queue}')

#     def stack(self):
#         temp = self.queue[1:]
#         self.queue = temp
#         print(f'Element removed: {self.head.medicalDate}\n{self.head}\n{self.queue}')



# # obj_MC = MedicalControl("Dr. Rojas", "Paciente con fractura en muñeca derecha, reco: Terapia F", "Rutinas poco peso, fuertes repeticiones", "todos los días", date(2022, 5, 7), 0.0, ['A5248','A9634', 'R9865'])
# # print(obj_MC)