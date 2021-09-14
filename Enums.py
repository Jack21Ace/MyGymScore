from enum import Enum
from typing import MutableMapping

#Eps = Enum('Eps', 'ASMETSALUD SURA MEDIMAS');
#Rh = Enum('Rh', 'O_POSITIVE O_NEGATIVE A_POSITIVE A_NEGATIVE B_POSITIVE B_NEGATIVE AB_POSITIVE AB_NEGATIVE UNSPECIFIED');
#Gender = Enum('Gender', 'MALE FEMALE NO-BINARY');
#Purpose = Enum('Purpose', 'REDUCE TONE_UP DEVELOP PHYSICAL_THERAPY CONDITIONING');

Type = Enum('Type', 'DISK BAR MANCUERNA RUBBER_BALL HEAVY_BALL ROPE MACHINE ELECTRIC PAD STOOL LOCKERS OFFICE');
ProductType = Enum('ProductType', 'PROTEIN AMINO_ACID SPORTSWEAR ACCESORIES SUPPLEMENTS HEALTHY_DRINKS HEALTHY_FOOD');
RoleList = Enum('RoleList', 'ADMINISTRATOR TRAINER NUTRITIONIST MAINTENANCE');
Ranking = Enum('Ranking', 'UNO DOS TRES CUATRO CINCO');
PayMethod = Enum('PayMethod', 'CASH CREDIT_CARD DEBIT_CARD WIRE_TRANSFER PAYPAL MOBYLE_PAY BONUSES');
UpperBody = Enum('UpperBody', 'DELTOIDS BICEPS TRICEPS TRAPEZE BACK ABDOMEN');
LowerBody = Enum('LowerBody', 'BUTTOCKS FEMORAL_BICEPS QUADRICEPS_FEMORIS TIBIAL CALF HAMSTRINGS');
Conditioning = Enum('Conditioning', 'WALK RUN JUMP SWIM SPINING_BIKE');

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

