import json
import re
import webbrowser


lista_nombres=[]
lista_edad=[]
lista_activo=[]
lista_promedio=[]
campos=["nombre","edad","activo","promedio"]

def main():
    opcion=""
    while("salir" not in opcion.lower()):
        print(">>>", end='')
        opcion = input()
        x=opcion.split(" ")
        opcionP=x[0].lower()
        if ("cargar" == opcionP):
            try:
                cadena = opcion[0:6]
                opcion = opcion.replace(cadena, "")
                opcion = opcion.replace(" ", "")
                arreglo2 = opcion.split(",")
                for i in arreglo2:
                    rutaa = i
                    Cargar(rutaa)
                    print("Archivo: ", i, " cargado")
            except:
                print("Algun archivo no encontrado")

        elif ("seleccionar" in opcionP):

            atributos=[]
            cadena=opcion[0:11]
            opcion=opcion.replace(cadena,"")
            arreglo=opcion.split(",")
            tamanio=len(arreglo)-1
            aste=opcion.replace(" ","")
            if(aste=="*"):
                print("")
                print(aste)
                asterisco()

            elif("*" in opcion and len(opcion)>5):
                opcion=opcion.replace("*","")
                opcion=pruebas(opcion)
                opcion=opcion[5:]
                opcion=pruebas(opcion)
                datos=opcion.split("=")
                atributoo=datos[0].replace(" ","").lower()
                condi=pruebas(datos[1])
                if atributoo in campos:
                    condi=condi.replace("'","")
                    condi=condi.replace("“","")
                    data=info(condi,campos)
                    print(data)
                else:
                    print("Error en Atributo")

            else:

                for i in range(tamanio):
                    local = arreglo[i].replace(" ", "")
                    local = local.lower()
                    atributos.append(local)

                elimardonde = arreglo[len(arreglo) - 1].split("=")
                x = re.findall("\A\s", elimardonde[0])
                c = elimardonde[0]
                z=""
                if x:
                    z = pruebas(c)
                else:
                    print("")
                condicion = elimardonde[1]
                condicion = condicion.replace(" ", "")
                condicion = condicion.replace("“", "")
                condicion = condicion.replace("”", "")
                condicion=condicion.replace("'","")

                valiodonde = z.split(" ", 1)
                ultimo_atributo = valiodonde[0]
                atributos.append(ultimo_atributo.lower())
                donde = valiodonde[1].split(" ", 1)
                atributo_condicion = donde[1].replace(" ", "")
                if ((len(atributo_condicion) > 8)):
                    atributo_condicion = atributo_condicion[5:]

                atributo_condicion = atributo_condicion.lower()
                bandera = Validar(atributos)
                if (bandera):
                    bandera2 = Validar2(atributo_condicion, campos)
                    if (bandera2):
                        if (atributo_condicion == "nombre"):
                            data = info(condicion, atributos)
                            print(data)
                        elif (atributo_condicion == "edad"):
                            data = info(condicion, atributos)
                            print(data)
                        elif (atributo_condicion == "activo"):
                            data = info(condicion, atributos)
                            print(data)
                        elif (atributo_condicion == "promedio"):
                            data = info(condicion, atributos)
                            print(data)
                    else:
                        print("Error campo de condicion")
                else:
                    print("Error Campos")

        elif ("maximo" in opcionP):
            cadena=opcion[0:6]
            opcion=opcion.replace(cadena,"")
            opcion=opcion.replace(" ","")

            if(opcion.lower()=="edad"):
                print(max(lista_edad))

            elif(opcion.lower()=="promedio"):
                print(max(lista_promedio))
            else:
                print("atributo no valido")

        elif ("minimo" in opcion.lower()):
            cadena = opcion[0:6]
            opcion = opcion.replace(cadena, "")
            opcion = opcion.replace(" ", "")
            if(opcion.lower()=="edad"):
                print(min(lista_edad))
            elif(opcion.lower()=="promedio"):
                print(min(lista_promedio))
            else:
                print("atributo no valido")

        elif ("cuenta" in opcionP):
            valor= sumaCuenta(lista_nombres)
            print(valor)

        elif(opcionP == "suma"):
            cadena = opcion[0:4]
            opcion=opcion.replace(cadena,"")
            opcion=opcion.replace(" ","")
            if(opcion.lower()=="edad"):
                valor=sumalista(lista_edad)
                print(valor)
            elif(opcion.lower()=="promedio"):
                valor=sumalista((lista_promedio))
                print(valor)
            else:
                print("Atributo no valido")

        elif ("reportar" in opcionP):
            opcion=opcion[8:]
            valorr=opcion.replace(" ","")
            n=int(valorr)
            if(n<=len(lista_nombres)):
                encabezado = '<!DOCTYPE html>\n' + '<html lang="en">\n' + '<head>\n' + '<meta charset="utf-8">\n' + '<title>Reporte</title>\n' + '<link rel="stylesheet"  href="tabla.css">\n'
                encabezado = encabezado + '</head>\n' + '<body>\n' + '<div id="main-container">\n' + '<table>\n' + '<thead>\n' + '<tr>\n'
                for element in campos:
                    temp = '<th>' + element + '</th>'
                    encabezado = encabezado + temp
                encabezado = encabezado + '\n</tr>' + '\n</thead>\n'
                for i in range(n):
                    etiqueta = '<tr>\n'
                    etiqueta = etiqueta + '<td>' + lista_nombres[i] + '</td><td>' + lista_edad[i] + '</td><td>' + \
                               lista_activo[i] + '</td><td>' + lista_promedio[i] + '</td>'

                    etiqueta = etiqueta + '\n</tr>\n'
                    encabezado = encabezado + etiqueta
                encabezado = encabezado + '</table>\n' + '</div>\n' + '</body>\n'

                fondo = "</html>"
                doc = open("index.html", "w")
                doc.write(encabezado)
                doc.write(fondo)

                doc.close()
                webbrowser.open_new_tab('index.html')

            else:
                print("Error ",n," mayor a los datos registrados")


        else:
            print("comando no reconocido")

def Cargar(rutaa):
    archivo = open(rutaa)
    info = json.load(archivo)
    archivo.close()

    for element in info:
        aux = str(element)
        aux = aux.replace("'", "")
        aux = aux.replace("{", "")
        aux = aux.replace("}", "")
        aux = aux.replace(":", "")
        aux = aux.replace(" ", "")
        arreglo = aux.split(",")
        arreglo[0]=arreglo[0].replace("nombre","")
        arreglo[1]=arreglo[1].replace("edad","")
        arreglo[2]=arreglo[2].replace("activo","")
        arreglo[3]=arreglo[3].replace("promedio","")
        lista_nombres.append(arreglo[0])
        lista_edad.append(arreglo[1])
        lista_activo.append(arreglo[2])
        lista_promedio.append(arreglo[3])
def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + float(i)
    return laSuma
def sumaCuenta(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + 1
    return laSuma
def pruebas(valor):
    txt = valor
    txt2=txt
    x = re.search("\A" + " ", txt)
    contador = 0
    while (x):

        x = re.search("\A"+" ", txt)
        txt = txt.replace(" ", "", 1)
        contador = contador + 1
    txt2=txt2.replace(" ","",(contador-1))


    return txt2
def Validar(lista_atributos):
    bandera = False
    for element in lista_atributos:
        if(element in campos):
            #print("Campo valido: ",element)
            bandera=True
        else:
           # print("Campo NO valido: ",element)
            bandera=False
            return bandera
    return bandera
def Validar2(atributo, campos):
    if(atributo in campos):
        bandera=True
        return bandera
    else:

        bandera=False
        return bandera
def info(condicion, atributos):
    data=""
    for i in range(len(lista_nombres)):
        if (condicion == lista_nombres[i]):
            index = i
            for element in atributos:
                if (element == "nombre"):
                    data = data + "Nombre: " + lista_nombres[index] + "\n"
                elif (element == "edad"):
                    data = data + "Edad: " + lista_edad[index] + "\n"
                elif (element == "activo"):
                    data = data + "Activo: " + lista_activo[index] + "\n"
                elif (element == "promedio"):
                    data = data + "Promedio: " + lista_promedio[index] + "\n"
            return data

        elif (condicion == lista_edad[i]):
            index = i
            for element in atributos:
                if (element == "nombre"):
                    data = data + "Nombre: " + lista_nombres[index] + "\n"
                elif (element == "edad"):
                    data = data + "Edad: " + lista_edad[index] + "\n"
                elif (element == "activo"):
                    data = data + "activo: " + lista_activo[index] + "\n"
                elif (element == "promedio"):
                    data = data + "Promedio: " + lista_promedio[index] + "\n"
            return data
        elif (condicion == lista_promedio[i]):
            index = i
            for element in atributos:
                if (element == "nombre"):
                    data = data + "Nombre: " + lista_nombres[index] + "\n"
                elif (element == "edad"):
                    data = data + "Edad: " + lista_edad[index] + "\n"
                elif (element == "activo"):
                    data = data + "Activo: " + lista_activo[index] + "\n"
                elif (element == "promedio"):
                    data = data + "Promedio: " + lista_promedio[index] + "\n"
            return data
        elif (condicion == lista_activo[i]):
            index = i
            for element in atributos:
                if (element == "nombre "):
                    data = data + "Nombre: " + lista_nombres[index] + "\n"
                elif (element == "edad"):
                    data = data + "Edad: " + lista_edad[index] + "\n"
                elif (element == "activo"):
                    data = data + "Activo: " + lista_activo[index] + "\n"
                elif (element == "promedio"):
                    data = data + "Promedio: " + lista_promedio[index] + "\n"
            return data
def asterisco():

    for i in range(len(lista_nombres)):
        index=i+1
        print("")
        print(index,".--------------------")
        print("nombre: ",lista_nombres[i])
        print("edad: ",lista_edad[i])
        print("activo: ",lista_activo[i])
        print("promedio: ",lista_promedio[i])
        print("----------------------")

main()