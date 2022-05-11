from MC_Queue import MC_Queue
from RoutineQueue import RoutineQueue
from UserQueue import UserQueue
from User import User
from Routine import Routine
from datetime import time, date
from MedicalControl import MedicalControl

if __name__ == '__main__':

    objUserQueue = UserQueue()
    objRoutineQueue = RoutineQueue()
    objMC_Queue = MC_Queue()

    # Objetos quemados de Rutinas
    rutinas:list = []
    r1 = Routine(102, 4, 15, 20.0, time(8, 30), "Acondicionamiento")
    r2 = Routine(202, 3, 10, 30.0, time(9, 45), "Tonificar")
    r3 = Routine(140, 4, 12, 10.0, time(10, 00), "Terapia Fisica")
    r4 = Routine(127, 6, 18, 0.0, time(13, 30), "Terapia Fisica")
    r5 = Routine(222, 3, 12, 40.0, time(16, 20), "Desarrollar")
    r6 = Routine(250, 3, 13, 20.5, time(5, 00), "Tonificar")
    r7 = Routine(300, 4, 10, 15.0, time(20, 40), "Acondicionamiento")
    rutinas = [r1,r2,r3,r4,r5,r6,r7]

    def routineQueue(rutinas):
        for e in rutinas:
            #print(e._routineId)
            objRoutineQueue.enqueue(e.routineId)

    def routineDequeue():
        objRoutineQueue.dequeue()

    def routineStack():
        objRoutineQueue.stack()

    mc_list:list = []
    mC1 = MedicalControl("Dr. Rojas", "Paciente de ingreso, reco: Acondicionamiento", "Rutina: Acondicionamiento Inicial", "1-Sem", date(2022, 5, 7), 0.0, ['A5800','A9645', 'R9865'])
    mC2 = MedicalControl("Dr. Rojas", "Paciente Sin novedad, reco: N/A", "Rutina: libre", "N/A", date(2022, 5, 7), 30.0, ['AB25844','C9634', 'E9865'])
    mC7 = MedicalControl("Dr. Rojas", "Paciente por revisión, reco: N/A", "Rutina: libre", "N/A", date(2022, 5, 7), 30.0, ['AB25844','C9634', 'E9865'])
    mC3 = MedicalControl("Dr. Rojas", "Paciente con mareos, reco: Tonificar", "Rutina: peso medido, fuertes repeticiones", "alternancia", date(2022, 5, 7), 23.5, ['A5248', 'RW961'])
    mC4 = MedicalControl("Dr. Cruz", "Paciente de competencia, reco: N/A", "Rutina: , fuertes repeticiones", "todos los días", date(2022, 5, 7), 15.0, [])
    mC5 = MedicalControl("Dr. Rojas", "Paciente con sobrepeso, reco: Acondicionamiento", "Rutinas poco peso, fuertes repeticiones", "todos los días", date(2022, 5, 7), 8.0, ['R9865'])
    mC6 = MedicalControl("Dr. Cruz", "Paciente con fractura en Femur Izq, reco: Terapia F", "Rutinas poco peso, fuertes repeticiones", "todos los días", date(2022, 5, 7), 3.5, ['A9634'])
    mc_list = [mC1, mC2, mC3 , mC4, mC5, mC6, mC7]

    def mc_Queue(mc_list):
        for e in mc_list:
        #print(e._routineId)
            objMC_Queue.enqueue(e.medicEmploName)

    def mc_Dequeue():
        objMC_Queue.dequeue()

    def mc_Stack():
        objMC_Queue.stack()

    # Objetos quemados de usuarios
    data:list=[]
    user1 = User("Victor", "Patiño", "13467925-T", "example@yahoo.com", "3010222555", 25, "O+", "Sura", [mC1])
    # user1.rutina = r1
    user2 = User("Julian", "Naranjo", "987654321", "3114445555", "porsospecha@hotmail.com", 48, "A-", "Medi+", [mC1])
    # user2.rutina = r4
    user3 = User("Sonia", "Herrera", "P-97642585", "3225285746", "profesalveme@yahoo.com", 33, 'AB+', "Salud Mortal", [mC3, mC4])
    # user3.rutina = r7
    user4 = User("James", "Soto", "1097642585", "3208948576", "aquinoesdonde@gmail.com", 21, "O+", "Sanitas", mc_list)
    # user4.rutina = r5
    user5 = User("Aroon", "Smith", "SW-1254873", "3200948006", "itsecurity@itsoft.sw", 21, "O+", "Sura", [])
    # user5.rutina = r3
    data:User = [user1, user2, user3, user4, user5]

    def userQueue(data):
        for e in data:
            #print(e.nombre)
            objUserQueue.enqueue(e.nombre)

    def userDequeue():
        objUserQueue.dequeue()

    def userStack():
        objUserQueue.stack()

    def options():
        opt = ''
        while (opt != 'x'):
            opt = str(input("Ingrese una de las siguientes opciones\n-----//-----//-----//-----//-----//-----//-----//-----\n1-) Usuarios\n2-) Rutinas\n3-) Control Medico\nX-) Salir\t").lower())
            if opt == 'x':
                print('Bye')
            elif opt == '1':
                opt_user = ''
                while (opt_user != 'x'):
                    print("\nIngrese una de las siguientes opciones")
                    print("-----//-----" * 4)
                    opt_user = str(input("1-) Quick Sort\n2-) Enqueue\n3-) Dequeue\n4-) Use Stack\n5-) Back\t").lower())
                    if opt_user == '1':
                        user1:User.optUsuarios(data)
                    elif opt_user == '2':
                        userQueue(data)
                    elif opt_user == '3':
                        userDequeue()
                    elif opt_user == '4':
                        userStack()
                    elif opt_user == '5':
                        print("Bye")
                        break
                    else:
                        print('Ingreso una opción erronea')
            elif opt == '2':
                print("\nIngrese una de las siguientes opciones")
                print("-----//-----" * 4)
                opt_Rut = ""
                while (opt_Rut != 'x'):
                    print("\nIngrese una de las siguientes opciones")
                    print("-----//-----" * 4)
                    opt_Rut = str(input("1-) Enqueue\n2-) Dequeue\n3-) Use Stack\n4-) Volver\t").lower())
                    if opt_Rut == '4':
                        print("Bye")
                        break
                    elif  opt_Rut == '1':
                        routineQueue(rutinas)
                    elif  opt_Rut == '2':
                        routineDequeue()
                    elif  opt_Rut == '3':
                        routineStack()
                    else:
                        print('Ingreso una opción erronea')
            elif opt == '3':
                print("\nIngrese una de las siguientes opciones")
                print("-----//-----" * 4)
                opt_MC = ""
                while (opt_MC != 'x'):
                    print("\nIngrese una de las siguientes opciones")
                    print("-----//-----" * 4)
                    opt_MC = str(input("1-) Enqueue\n2-) Dequeue\n3-) Use Stack\n4-) Volver\t").lower())
                    if opt_MC == '4':
                        print("Bye")
                        break
                    elif  opt_MC == '1':
                        mc_Queue(mc_list)
                    elif  opt_MC == '2':
                        mc_Dequeue()
                    elif  opt_MC == '3':
                        mc_Stack()
                    else:
                        print('Ingreso una opción erronea')
            else:
                print('Ingreso una opción erronea')
    options()