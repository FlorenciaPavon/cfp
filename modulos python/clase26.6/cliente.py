
from cajero import Cajero

class Cliente:
    def __init__(self,cuenta, pin,  nom=""):
        self.__nomnbre= nom
        
        self.__nCuenta= cuenta

    def sacarDinero(self):        
        ca=Cajero(1234)

        ticket= ca.darDinero(self.__nCuenta)
        print("Hola", self.__nomnbre, ", esta es tu extraccion:")
        print (ticket)

    def depositar(self, nCuenta):
        pass
   
    def consultar(self):
        ca=Cajero(1234)
        consulta= ca.mostrarSaldo(self.__nCuenta)
        print("Hola", self.__nomnbre, ", aquí su consulta:")
        print (consulta)
