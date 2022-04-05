from enum import Enum

# Enumeración Eps
class Eps(Enum):
    ASMETSALUD = "Asmet Salud"
    SURA = "Sura"
    MEDIMAS = "Medimas"
    SALUDMORTAL = "Salud Mortal"

# Enumeración RH
class Rh(Enum):
    O_POSITIVE = 'O+'
    O_NEGATIVE = 'O-'
    A_POSITIVE = 'A+'
    A_NEGATIVE = 'A-'
    B_POSITIVE = 'B-'
    B_NEGATIVE = 'B+'
    AB_POSITIVE = 'AB+'
    AB_NEGATIVE = 'AB-'

class UpperBody(Enum):
    DELTOIDS = 'Deltoides'
    BICEPS = 'Biceps'
    TRICEPS = 'Triceps'
    TRAPEZE = 'Trapecio'
    BACK = 'Espalda'
    ABDOMEN = 'Abdomen'

# Enumeracion TRONCO INFERIOR
class LowerBody(Enum):
    BUTTOCKS = 'Gluteos'
    FEMORAL_BICEPS = 'Biceps Femoral'
    QUADRICEPS_FEMORIS = 'Quadriceps Femoral'
    TIBIAL = 'Tibial'
    CALF = 'Pantorrilla'
    HAMSTRINGS = 'Isquiotibiales'

# Enumeracion ACONDICIONAMIENTO
class Conditioning(Enum):
    WALK = 'Caminata'
    RUN = 'Correr'
    JUMP = 'Saltar'
    SWIM = 'Nadar'
    SPINING_BIKE = 'Bicicleta Estatica'