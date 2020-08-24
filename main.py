import json


def main():
    opcion=""
    while(opcion.lower()!="salir"):
        print(">>>", end='')
        opcion = input()
        if (opcion.lower() == "cargar"):
            print("opcion cargar")
        elif (opcion.lower() == "seleccionar"):
            print("opcion seleccionar")
        elif (opcion.lower() == "maximo"):
            print("opcion maximo")
        elif (opcion.lower() == "minimo"):
            print("opcion minimo")
        elif (opcion.lower() == "cuenta"):
            print("opcion minimo")
        elif (opcion.lower() == "reportar"):
            print("opcion reportar")
        else:
            print("comando no reconocido")



def Cargar(ruta):
        archivo = open(ruta)
        info = json.load(archivo)
        archivo.close()
        print("")
        print(info)
        return (info)
        des = Cargar_Json(ruta)
        for element in des:
            paso=0
            print("")
            print(element+" "+paso)
            paso+=paso+1


main()