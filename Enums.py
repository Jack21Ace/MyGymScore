from enum import Enum
#from typing import MutableMapping

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

# Enumeración Gender
class  Gender(Enum):
    FEMALE = 'Femenino'
    MALE = 'Masculino'
    NO_BINARY = 'No binario'

# Enumeración Purpose
class Purpose(Enum):
    REDUCE = 'Reducir'
    TONE_UP = 'Tonificar'
    DEVELOP = 'Desarrollar'
    PHYSICAL_THERAPY = 'Terapia Fisica'
    CONDITIONING = 'CONDITIONING'

# Enumeracion Metodo de pago 
class PayMethod(Enum):
    CASH = 'CASH'
    CREDIT_CARD = 'Tarjeta de Credito'
    DEBIT_CARD = 'Tarjeta de Debito'
    WIRE_TRANSFER = 'Transferencia Bancaria'
    PAYPAL = 'PAYPAL'
    MOBYLE_PAY = 'Pagos Moviles'
    BONUSES = 'Bonos'

# Enumeracion TRONCO SUPERIOR 
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

# Enumeración Type
class Type(Enum):
    DISK = "Disco"
    BAR = "Barra"
    MANCUERNA = "Mancuerna"
    RUBBER_BALL = "Pelota de goma"
    HEAVY_BALL = "Bola Pesada"
    ROPE = "Soga"
    MACHINE = "Máquina"
    ELECTRIC = "Eléctrico"
    PAD = "Almohadilla"
    STOOL = "Taburete"
    LOCKERS = "Casilleros"
    OFFICE = "Oficina"

# Enumeración Tipo del Producto
class AccessoryType(Enum):
    BOTTLE = "Bottle"
    T_SHIRT = "T_Shirt"
    SHORT = "Short"
    GLOVES = "Gloves"
    VANDAGES = "Vandages"
    WEIGHT_BELT = "Weight Belt"
    TOWEL = "Towel"

# ConsumableType Enumaration
class consumableType(Enum):
    PROTEIN = "Protenina"
    AMINO_ACID = "Aminoacidos"
    VITAMINE = "Vitaminas"
    COLLAGENE = "Colageno"
    GLUTAMINE = "Glutamina"
    BANANA = "Bananos"
    BOCADILLO = "Bocadillo"
    JUICE = "Jugo"
    CREATINE = "Queratina"
    SNACK = "Barra de proteina"

# Enumeración RoleList
class Role(Enum):
    ADMINISTRATOR = "Administrador"
    TRAINER = "Entrenador"
    NUTRITIONIST = "Nutricionista"
    MAINTENANCE = "Mantenimiento"

# Enumeración del Ranking
class Ranking(Enum):
    UNO = "Uno"
    DOS = "Dos"
    TRES = "Tres"
    CUATRO = "Cuatro"
    CINCO = "Cinco"