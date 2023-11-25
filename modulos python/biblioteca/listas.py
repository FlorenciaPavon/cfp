def cargarLista(ls):
    ls.append([1234, "Juan Lopez"])
    ls.append([9454, "Juana Lopez"])
    ls.append([45545, "Maria Lopez"])

def imprimirLista(ls):
    for linea in ls:
        print("{:7} {:>20}".format (linea[0], linea[1] ))