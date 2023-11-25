class Banco:
    def __init__(self):
        self.__nombre= "Nación"
        self.__nCuenta={12:["Juan", 1234, 10],
                        63:["Laura", 9996, 20],
                        101:["Clara", 7788, 320]}

    def validarCliente(self, nCuenta, clave):
        res=[]
        di = self.__nCuenta

        if di.get(nCuenta)!=None:
            if di.get(nCuenta)[1]==clave:
                res=di.get(nCuenta)
        return res

# b=Banco()
# lsRes= b.validarCliente(12,1234)
# print(lsRes)