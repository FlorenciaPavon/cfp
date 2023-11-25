from persona import Persona
#supuse el mismo boton para encendido y apagado
class Remoto:
    def __init__(self):
        self.__onOff= ""  #true= encendido false=apagado
    
    def onOf(self, decision):
        p=Persona(decision)
        if p.encenderTV()==True:
            self.__onOff= True
        else:
            p.apagarTV()
            self.__onOff= False
        return self.__onOff
    
    def tecladoCanal(self, canal, decision):
        p=Persona(decision)
        p.cambiarCanal(canal)
        
    def mostrarPantalla(self):
        p=Persona(decision)
        p.verPantalla()
#         pantalla=""
#         if self.__onOff == "boton Prender":
#             pantalla = True
#         else:
#             pantalla = False            
#         return pantalla
    
    def getOnOff(self):
        return self.__onOff
        
# def main():
#     r=Remoto()
#     print(r.onOf("no"))
#     print(r.tecladoCanal(32))
#     print(r.mostrarPantalla())
# main()    