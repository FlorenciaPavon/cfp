from remoto import Remoto
import random

class Televisor:
    def __init__(self):
        self.__ubicacion:""
        self.__estado:""
        self.__canal:""
    
    def apagar(self):
        r=Remoto()
        r.onOf("no")
        self.__estado = "TV apagada"
        return self.__estado

    def encender(self):
        r=Remoto()
        r.onOf("si")
        self.__estado= "TV prendida"
        return self.__estado 
    
            
    def mostrar(self):       
        self.__ubicacion = ["El living", "La cocina", "El dormitorio"]
        if self.__estado == "TV prendida":
            return random.choice(self.__ubicacion)
        
    def canal(self, canal, decision):
        r=Remoto()
        r.tecladoCanal(canal, decision)
        self.__canal = r.tecladoCanal(canal, decision)
        return  self.__canal
        
             
# def main():             
#     t=Televisor()
#     print(t.encender())
#     print(t.mostrar())
# main()