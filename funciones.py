import json
from logging.config import dictConfig
import sys

def leer_json(fichero):
    try:
        with open(fichero) as f:
            datos=json.load(f)
        return datos
    except:
        print("Error al leer el fichero")
        sys.exit(0)

def listar_animes(datos):
    lista=[]
    for listas in datos:
        lista.append(listas.get("title").get("text"))
    return lista

def contar_estudios(datos):
    lista=[]
    for listas in datos:
        if listas.get("studio") not in lista:
            lista.append(listas.get("studio"))
    return lista , len(lista)

#3. Pide por teclado un anime y muestra el estudio que lo realiza.

def mostrar_estudios(datos,estudios):
    for animes in datos:
        titulo=animes.get("title").get("text")
        if titulo == estudios:
            return animes.get("studio")

#4. Pedir por teclado un genero y mostrar los animes que pertenecen a el.

def mostrar_animes(datos,animes):







































































#def elegir(lista_de_opciones):
#    num = 1
 ##   for opcion in lista_de_opciones:
  #      print(f"Opción {str(num)}: {str(opcion)}")
   #     num += 1
#    opcion_elegida = input("\nEscriba el número de su opción y pulse ENTER: ")
#    print("")
#    num = 0
#    for opcion in lista_de_opciones:
#        num += 1
#        opcion_actual = str(num)
 ##       if opcion_elegida == opcion_actual:
#            return opcion
#    input("La opción elegida no existe. Pulse ENTER para volver al menú principal.")
    
#def listar(info_json):
#    print("Lista de animes:\n")
##    contador=0
#    for nombre_anime in list(info_json.keys()):
#        name_anime= info_json.get(nombre_anime)
#        for anime in name_anime:
##            nombredeanime= anime.get("title")
#            print(nombredeanime)
