class Persona:
    def __init__(self, decision):        
        self.__decision=decision
        self.__apagar=""
        self.__canal=""
        self.__mirar=""
        
    
    def encenderTV(self):
        if self.__decision=="Si" or self.__decision=="si":
            res = True
        else:            
            res = False
        return res
    
    def apagarTV(self):
        if self.encenderTV()==False:
            self.__apagar==True
        else:
            self.__apagar = "no puedo apagarla persona"
        return self.__apagar
    
#     def apagarTV(self):
#         if self.encenderTV():
#             return "quiero apagar la tele"
#         else:
#             return "no puedo apagarla porque no la prendí"
    
    def cambiarCanal(self, canal):
        if self.encenderTV():
            self.__canal: canal            
        else:
            self.__canal="no puedo cambiar de canal porque no la prendí Persona"
        return self.__canal
        
    def verPantalla(self):
        if self.encenderTV():            
            self.__mirar= True
        else:
            self.__mirar= "Persona estoy viendo una pantalla apagada"
        return self.__mirar
# 
# def main():
#     p=Persona("no")
#     p.encenderTV()
#     print(p.apagarTV())
#     print(p.cambiarCanal(52))
#     print(p.verPantalla())
# main()