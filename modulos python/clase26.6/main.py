
from cliente import Cliente



class Banco():
    #va a verificar que la clave sea la del cliente (dicc)
    #tiene la informacion de las cuentas

    def __init__(self):
        pass

'''
agregar la clase banco que tiene la informacion de cuentas
saldos claves y nro de cliente y modelar una extraccion y una consulta de
saldo de un cliente que accede a un cajero
'''

def main():
    # armo un cliente
    #pruebas con pin 1234,  4569 y 9368
    #pruebas con nro cuenta 89899, 632145 y 321547
    cl1=Cliente("89899", 1234)
    cl1.consultar()
    cl1.sacarDinero()
main()