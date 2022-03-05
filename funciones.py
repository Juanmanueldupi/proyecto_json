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
    for anime in datos:
        lista.append(anime.get("title").get("text"))
    return lista

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
    
