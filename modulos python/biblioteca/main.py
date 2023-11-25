#para importar primero hay que crear el archivo __init__.py
from biblioteca import diccionarios
from biblioteca import listas



def main():
    ls=[]
    di={}
    print("LISTA")
    cargarLista(ls)
    imprimirLista(ls)
    print("DICCIONARIO")
    cargarDic(di)
    imprimirDic(di)

main()