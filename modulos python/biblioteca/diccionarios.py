def cargarDic(di):
    di[1234] = "Juan Lopez"
    di[9454] = "Juana Lopez"
    di[45545] = "Maria Lopez"

def imprimirDic(di):
    for k in di:
        print("{:7} {:>20}".format (k, di[k]))        