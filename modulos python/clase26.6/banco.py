'''
agregar la clase banco que tiene la informacion de cuentas
saldos claves y nro de cliente y modelar una extraccion y una consulta de
saldo de un cliente que accede a un cajero
'''
class Banco():
    def __init__(self, nCuenta, pinCaj):        
        #datosDi={nCuenta= [clave, saldo]}
        self.__datosDi={89899:[1234, 150000],
                 632145:[4569, 300],
                 321547:[9368, 250000]}
        self.__nCuenta = nCuenta
        self.__claveCaj= pinCaj
        
    def verifDatos(self):
        if self.__datosDi[self.__nCuenta][0]== self.__claveCaj:
            res=True
        else:
            res= False
        return res
    

    if verifDatos()==True:
        
        @property
        def saldo(self):
            datos= self.__datosDi
            cuenta= self.__nCuenta
            for k in datos:
                saldo = datos[cuenta][1]
            return saldo
            
        @saldo.setter
        def nuevoSaldo(self, nSaldo):
            datos= self.__datosDi
            cuenta= self.__nCuenta
            for cuenta in datos:
               datos[cuenta][1] = nSaldo
            



