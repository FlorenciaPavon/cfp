from banco import Banco

class Cajero:
    def __init__(self):
        self.__red="Banelco"
        self.__ubicacion="Av. Rivadavia 7030"

    def mostrarSaldo(self, nCuenta, clave):
        lsRes = self.__solicitarPermisos(nCuenta, clave)
        if lsRes != []: 
            saldo = lsRes[2]
        else:
            saldo=None
        return saldo
        

    def darDinero(self, monto, nCuenta, clave):
        pass

    def solicitarPermisos(self, nCuenta, clave):
        b = Banco()
        lsRes = b.validarCliente(nCuenta, clave)
        return lsRes
    
c=Cajero()
print(c.solicitarPermisos(12, 1234))
