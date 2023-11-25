class Usuario:
    def __init__(self, id=54, nom="Mariela", ape="Gomez", dni=5456, email="", cont=""):
        self.__id=id	
        self.__nombre= nom
        self.__apellido= ape
        self.__dni=dni	
        self.__email=email
        self.__contrasena=cont
        
#     getters y setters
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nom):
        self.__nombre = nom
        
    def getApellido(self):
        return self.__apellido
    def setApellido(self, ape):
        self.__apellido = ape
        
    def getDni(self):
        return self.__dni
    def setDni(self, dni):
        self.__dni=dni
        
    def getEmail(self):
        return self.__email
    def setEmail(self, email):
        self.__email=email
        
    def setContrasena(self, cont):
        self.__contrasena=cont

# metodos        
    def cambiarPerfil(self):
# modifico los atributos de la clase
        pass
    
    