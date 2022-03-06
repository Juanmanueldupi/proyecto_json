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


#Menu

def MostrarMenu():
    menu='''
    1. Lista el nombre de los animes.
    2. Contar todos los estudios. 
    3. Pide por teclado un anime y muestra el estudio que lo realiza.
    4. Pedir por teclado un genero y mostrar los animes que pertenecen a el.(Action,Mystery,Seinen,Supernatural,Comedy,Ecchi,Fantasy,Harem,Romance,School,Sci-Fi,Super Power,Drama,Military,Police,Magic,Adventure,Slice of Life,Demons,Mecha,Horror,Space,Ai)
    5. Pide por teclado un estudio y te muestra los animes realizados(si hay mas de uno, muestra todos) y su descripcion.
    6. Salir
    '''
    print(menu)
    while True:
        try:
            opcion=int(input("Opción:"))
            return opcion
        except:
            print("Opción incorrecta, debe ser un número")

# 1. Lista el nombre de los animes.

def listar_animes(datos):
    lista=[]
    for anime in datos:
        lista.append(anime.get("title").get("text"))
    return lista

# 2. Contar todos los estudios. 

def listar_estudios(datos):
    lista=[]
    for anime in datos:
        lista.append(anime.get("studio"))
    return lista


def contar_estudios(datos):
    lista=[]
    for anime in datos:
        if anime.get("studio") not in lista:
            lista.append(anime.get("studio"))
    return len(lista)

#3. Pide por teclado un anime y muestra el estudio que lo realiza.

def mostrar_estudios(datos,estudios):
    for anime in datos:
        titulo=anime.get("title").get("text")
        if titulo == estudios:
            return anime.get("studio")

#4. Pedir por teclado un genero y mostrar los animes que pertenecen a el.

#def listar_generos(datos):
#    lista=[]
#    for genero in datos:
#        lista.append(genero.get("genres"))
#    return genero

def mostrar_animes(datos,genero):
    lista=[]

    for anime in datos:
        nombres=anime.get("genres")
        for nombre in nombres:
            if nombre == genero:
                lista.append(anime.get("title").get("text")) 


    return lista


#5. Pide por teclado un estudio y te muestra los animes realizados(si hay mas de uno, muestra todos) y su descripcion.


def mostrar_animes_por_estudio(datos,estudio):
        lista=[]
        

        for anime in datos:
            estudio_anime=anime.get("studio")
            if estudio == estudio_anime:
                    lista.append(anime.get("title").get("text"))
                    lista.append(anime.get("description"))
                    lista.append("")

        return lista
    
