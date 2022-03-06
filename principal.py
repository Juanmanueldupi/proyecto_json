from funciones import *

info_json= leer_json("animes.json")

opcion=MostrarMenu()
print()
while opcion != 6:
    if opcion == 1:
        for anime in listar_animes(info_json):
            print(anime)
    if opcion == 2:
        for estudio in listar_estudios(info_json):
            print(estudio)
        print()    
        print("El numero de estudios es: ",contar_estudios(info_json))
    if opcion == 3:
        estudios = input("Introduce un anime para ver el estudio que lo realiza: ")
        print()
        print("El estudio que realiza este anime es: ", mostrar_estudios(info_json,estudios))
    if opcion == 4:
        genero = input("Introduce un genero para ver los animes que pertenezcan a ese genero: ")
        print()
        listaAnimesPorGenero = mostrar_animes(info_json,genero)
        print("Animes correspondientes al genero introducido: " )
        print()
        for anime in listaAnimesPorGenero:
            print(anime)
    if opcion == 5:
        estudio= input("Introduce un estudio para ver los animes que pertenezcan a dicho estudio y su descripción: ")
        print()
        lista = mostrar_animes_por_estudio(info_json,estudio)
        print("Animes y su descripción: ")
        print()
        for anime in lista:
            print()
            print(anime)
    if opcion == 6:
        print("Salir del programa")  
        print()

    opcion=MostrarMenu()
    print()