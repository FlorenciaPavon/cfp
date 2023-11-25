from cajero import Cajero

class Cliente:
    def __init__(self,nom, cuenta, clave):
        self.__nombre=nom       
        self.__nCuenta= cuenta
        self.__clave=clave

    def sacarDinero(self):
        pass

    def depositar(self):
        pass

    def consultar(self):
        ca=Cajero()
        consulta = ca.mostrarSaldo(self.__nCuenta, self.__clave)
        if consulta != None:
            print ("Hola", self.__nombre, "Aquí tu consulta: ")
            print(consulta)
        else:
            print("ERROR!!")