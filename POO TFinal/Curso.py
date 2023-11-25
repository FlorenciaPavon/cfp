class Curso:
    def __init__(self, nom, turno, vac, doc):
        self.__nombre=""
        self.__turno=""
        self.__cantVacante=0
        self.__docente=""

# getters y setters
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nom):
        self.__nombre = nom
        
    def getTurno(self):
        return self.__turno
    def setTurno(self, turno):
        self.__turno= turno
        
    def getVac(self):
        return self.__cantVacante
    def setVac(self, vac):
        self.__cantVacante=vac
        
    def getDocente(self):
        return self.__docente
    def setDocente(self, doc):
        self.__docente= doc

# metodos    
    def crearCurso(self, nombreCurso, turno, cantVacante, docente):
        pass
    
    def modificarCurso(self, cantVacante, docente):
        pass