from random import randint
from banco import Banco

class Cajero:
    def __init__(self, pinCaj,  red="Banelco", ubi="Av Rivadavia 221"):
        self.__red= red
        self.__ubicacion= ubi
        self.__claveCaj= pinCaj
        
    def verificacion(self, nCuenta):
        b1=Banco(nCuenta, self.__claveCaj)
        b1.verifDatos()

    def mostrarSaldo(self, nCuenta):
        # saldo=randint(0, 9999)
        b1=Banco(nCuenta, self.__claveCaj)

        if b1.VerifDatos()==True:
            saldo= self.__datosDi[self.__nCuenta][1]

            salida= "Su cuenta {} tiene : {}$".format (nCuenta, saldo )
            return salida

    def darDinero(self, nCuenta):
        valor=randint(0,9999)
        b1=Banco()

        if b1.verifDatos()==True:
            saldo= self.__datosDi[self.__nCuenta][1]
            saldo -=  valor
            res="Se entregaron {}$ desde la cuenta {}".format (valor, nCuenta)
            return res