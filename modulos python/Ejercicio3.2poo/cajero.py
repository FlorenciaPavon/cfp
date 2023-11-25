from banco import Banco


class Cajero:
    def __init__(self):
        self.__red="Banelco"
        self.__ubicacion="Av Rivadavia 6750"
    
    def mostrarSaldo(self, nCuenta, clave):
        if self.__solicitarPermisos(nCuenta, clave) != False:
            b=Banco()
            return b.accederSaldo(nCuenta)
        else:
            print("Datos incorrectos")
            
            
    def darDinero(self, monto, nCuenta, clave):
        if self.__solicitarPermisos(nCuenta, clave) != False:
            b=Banco()
            saldo = b.accederSaldo(nCuenta)
            extraccion = saldo - monto
            print(extraccion)
        else:
            print("Datos incorrectos")
           
    
    def __solicitarPermisos(self, nCuenta, clave):  #privado
        b=Banco()
        validacion= b.validarCliente(nCuenta, clave)
        return validacion
    
    def accederPermisos(self, nCuenta, clave):
        return self.__solicitarPermisos(nCuenta, clave)
     
# def main():
#     c=Cajero()
#     c.darDinero(5,12,45646)
    
#     
#     #cliente con datos correctos
#     c.accederPermisos(12, 1234)
#     print(c.mostrarSaldo(12, 1234))
#     print(c.mostrarSaldo(63, 9996))
#	  c.darDinero(5,12,1234)

#      #cliente con pin incorrecto
#     c.accederPermisos(12, 4545)
#     print(c.mostrarSaldo(63, 456454))

#     #cliente con cuenta y pin inexistentes
#     c.accederPermisos(56456, 2123)
# main()