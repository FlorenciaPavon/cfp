# from datetime import timedelta
# from datetime import datetime
# 
# '''
# Programa diseñado para usuario comercial bancario (empleado)
# '''
# 
# class Cuenta:    
#     def __init__(self):
#         self.__nCuenta=54654
#         self.__nombre="Marianela Perez"
#         self.__saldo=2000
#         self.__tipoCuenta="Caja de ahorros"
# #        self.__fechaDep= datetime(2023, 1, 24) #caso de prueba 2.1: fecha de deposito MAYOR a 30 días menos de hoy
#         self.__fechaDep= datetime(2023, 5, 31) #caso de prueba 2.2: fecha de deposito MENOR a 30 días menos de hoy
#            
#     @property
#     def fechaDep(self):  
#         return self.__fechaDep
#     
#     @property
#     def saldo(self):
#         return self.__saldo
#  
#  
#     def depositar(self, val):
#         self.__saldo += val
#         return self.__saldo
# 
#     def retirar(self, val):
#         self.__saldo -= val
#         return self.__saldo
#     
#     def consultarDatos(self):
#         datos = "Nombre: {}, Cuenta: {}, Saldo: {}". format (self.__nombre, self.__tipoCuenta, self.__saldo)
#         return datos
#     
# class Ahorro(Cuenta):    
#     def __init__(self, saldoPzoFijo):
#         super().__init__()        
#         self.__pInterMens=0.6
#         self.__plazoFijo=saldoPzoFijo
# 
#     def depositarInteres(self):
#         saldoPzoFijo= self.__plazoFijo
#         
#         hoy=datetime.today()        
#         fechaDeposito=super().fechaDep
#         vto=timedelta(days=30)
#         fechaVenc= fechaDeposito + vto        
#         
#         if fechaVenc < hoy and saldoPzoFijo != 0:
#             interes= saldoPzoFijo*(1 + self.__pInterMens)
#             res= super().depositar(interes)            
#         elif fechaVenc > hoy and saldoPzoFijo != 0:
#             res= "No ha pasado el plazo mínimo de 30 días."
#         elif saldoPzoFijo == 0:
#             res= "No posee saldo en el Plazo Fijo."
#         return res
# 
# class Cheques(Cuenta):
#     def __init__(self):
#         super().__init__()
#         self.__comisionUso=0.01
#         self.__comisionSinFondos=0.1
# #        self.__montoDebitoCheque=500
#         self.__montoDebitoCheque=5000
# 
#     def descuentoComision(self):
#         saldo= super().saldo
#         if saldo >= self.__montoDebitoCheque:            
#           comUso= self.__montoDebitoCheque * (1 + self.__comisionUso)
#           res= super().retirar(comUso)
#           print("Se descontará el total de: ", comUso)
#         else:
#           comSinSaldo=self.__montoDebitoCheque * (1 +self.__comisionSinFondos)
#           res=super().retirar(comSinSaldo)
#           print("Sin saldo, se descontará y quedará descubierto: ", comSinSaldo)
#         return res
# 
#     def depositarCheque(self, val):
#         print ("Se depositó el cheque 54564 con monto: ", val)
#         return super().depositar(val)        
# 
# def main():
#     print("-"*60)
#     print("Transacciones de la Cuenta")
#     print("-"*60)
#     c1=Cuenta()
#     print("Depósito: ", c1.depositar(200))
#     print("Retiro: ",c1.retirar(100))
#     print("Datos: ", c1.consultarDatos())
#     print()
# #-------------------------------------------------------#  
# #depósito de interés con saldo en la cuenta de plazo fijo
#     print("-"*60)
#     print("Transacciones de Caja de Ahorro/ Plazo Fijo")
#     print("-"*60)
# #caso 1: tiene saldo en el plazo fijo. Ver en los atributos de cuenta los dos casos adicionales.
# #     c1=Ahorro(1000)
# #     print("Depósito de interes: ", c1.depositarInteres())
# #	  print()45
# 
# #caso 2: que tenga saldo en la caja de ahorros, pero no invertido en el plazo fijo    
#     c2=Ahorro(0)    
#     print("Depósito de interes: ", c2.depositarInteres())
#     print()
# #-------------------------------------------------------#
#     print("-"*60)
#     print("Transacciones de Cuenta Corriente/ Cheques")
#     print("-"*60)
#     c1=Cheques()
# # Descuento por uso de chequera
#     print("Saldo: ", c1.descuentoComision())
#     print()
# # Depósito de cheque
#     print("Saldo: ", c1.depositarCheque(1000))
# 
# main()