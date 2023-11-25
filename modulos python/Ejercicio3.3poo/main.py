from remoto import Remoto
from persona import Persona
from televisor import Televisor

def main():
    print("Desea mirar tele?")
    print("Ingrese si o no en la siguiente opción")
    dec=input("Si/No: ")
    
    p=Persona(dec)
    r=Remoto()    
    t=Televisor()
    
    print("-" * 10)
    print(r.onOf(dec))
    print("{} en {}". format(t.encender(), t.mostrar()))    
    print("-" * 10)
    
    print("Que más desea hacer?")
    print()
    print("1 - Cambiar de canal")
    print("2 - Apagar la tele")
    print("3 - Mirar tele")
    op=int(input("Ingrese el nro de la opción: "))
    
    if op == 1:        
        canal=int(input("Ingrese el canal: "))
        t.canal(canal, dec)
        print("Cambio de canal a: canal ", canal )
    elif op == 2:
        p=Persona("no")
        r.onOf("no")
        print(t.apagar())
    elif op == 3:
        p.verPantalla()
        if p.verPantalla()==True:
            print("Me quedo a ver la tele")
    else:
        print()
        print("Informacion incorrecta, será dirigido")
   
main()   