class Banco:
    def __init__(self):
        self.__nombre= "Banco Nación"
        self.__nCuenta= {12:["Juan", 1234,100],    #nCuenta:[nombre, pin, saldo]
                         63:["Laura", 9996, 200],
                         101: ["Clara", 7788, 3200]}
        
    def validarCliente(self, nCuenta, clave):
        cuentasDicc= self.__nCuenta
        if nCuenta !=0:
            if nCuenta in cuentasDicc and cuentasDicc[nCuenta][1]== clave:
                res= True
            else:
                res= False
        else:
            res= False
        return res
    
    def __nombre(self, nCuenta):
        cuentasDicc= self.__nCuenta
        nombre= cuentasDicc[nCuenta][0]
        return nombre
    def accederNombre(self, nCuenta):
        return self.__nombre(nCuenta)
        
    def __saldo(self, nCuenta):
        cuentasDicc= self.__nCuenta
        saldo= cuentasDicc[nCuenta][2]
        return saldo
    def accederSaldo(self, nCuenta):
        return self.__saldo(nCuenta)
            
# def main():
#     b=Banco()
#     #cliente correcto
#     print(b.validarCliente(12, 1234))
# #     #cliente con pin incorrecto
#     print(b.validarCliente(12, 3334))
# #     #cliente con cuenta y pin inexistentes
#     print(b.validarCliente(1, 4544))
#    # b.validarCliente()
# main()