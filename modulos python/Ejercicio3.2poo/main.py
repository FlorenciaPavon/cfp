from banco import Banco
from cajero import Cajero
from cliente import Cliente

#
# self.__nCuenta= {12:["Juan", 1234,10],    #nCuenta:[nombre, pin, saldo]
#                          63:["Laura", 9996, 20],
#                          101: ["Clara", 7788, 320]}


def main():
    print("=" * 40)
    print("Bienvenido al Banco Nación")
    print("=" * 40)
    print("Ingrese los siguientes campos:")
    print()
    nCuenta= int(input("Número de cuenta: " ))
    clave= int(input("PIN: " ))
    
    c=Cajero()
    permiso= c.accederPermisos(nCuenta, clave)
    
    if permiso == True:
        print("Elija la opción deseada")        
        print()
        print("1 - Depósito en su misma cuenta")
        print("2 - Extracción")
        print("3 - Consulta de saldo")
        print()
        op=int(input("Ingrese el número de su opción: "))   
        
        if op==1:
            monto=int(input("Ingrese el monto a depositar: "))
            c=Cliente()
            print("Se depositó $", monto, "Su saldo actual es: ")
            c.depositar(monto, nCuenta, clave)
        elif op==2:
            monto=int(input("Ingrese el monto a extraer: "))
            c=Cliente()
            print("Se extrajo $", monto, "Su saldo actual es: ")
            c.sacarDinero(monto, nCuenta, clave)
        elif op==3:
            c=Cliente()
            saldo = c.consultar(nCuenta, clave)
            print("Su saldo acutal es $", saldo)
        else:
            print()
            print("----------Opción incorrecta, será redirigido-----------")
            print()
            main()
        
    else:
        print ("Datos incorrectos!!")
        print("Desea continuar?")
        print("1 - Si")
        print("2 - No")
        n= int(input("Elija el número de la opción deseada: "))
        if n == 1:
            main()
        else:
            print("Gracias por operar con Banco Nación")
main()    
    