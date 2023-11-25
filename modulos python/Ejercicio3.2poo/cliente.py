from cajero import Cajero

class Cliente:
    def __init__(self):
        #para acceder a estos datos debería poder acceder a Banco, pero
        #primero pasa por cajero por lo que no se puede importar
        self.__nombre=""
        self.__dni=""
        
    def sacarDinero(self, monto, nCuenta, clave):
        c=Cajero()
        c.darDinero(monto, nCuenta, clave)
    
    #supongo que el cliente hace un deposito en su misma cuenta, por eso pide clave
    def depositar(self, monto, nCuenta, clave ):                                       
            c=Cajero()
            saldo= c.mostrarSaldo(nCuenta, clave)
            #EXPLICACION DEL IF
            #en el método anterior, si los datos están validados, obtengo un int que es el saldo. 
            #Si no esta validado obtengo una cadena de caracteres "Datos incorrectos".
            #Por lo que si en el caso de prueba pongo los datos incorrectos, trata de hacer la suma
            #de un int y un str, y da error de "invalid operation"
            if type(saldo)==int:
                deposito = saldo + monto
                print(deposito)
            else:
                print("Datos incorrectos")
        
    
    def consultar(self, nCuenta, clave):
        c=Cajero()
        return c.mostrarSaldo(nCuenta, clave)
            
        
#     
# def main():
#     cl=Cliente()
#	  #cliente correcto
#     print(cl.consultar(12,1234))
#	  #clave incorrecta
#     cl.sacarDinero(20, 12, 54564)
#     cl.depositar(20,12,1234)
#	  #clave incorrecta
#     cl.depositar(20,12,45646)
# main()
    