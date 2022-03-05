from funciones import *

info_json= leer_json("animes.json")

menu= '''
Menu:
1. Lista el nombre de los animes.
2. Contar todos los estudios. 
3. Pide por teclado un anime y muestra el estudio que lo realiza.
4. Pedir por teclado un genero y mostrar los animes que pertenecen a el.
5. Pide por teclado un estudio y te muestra los animes realizados(si hay mas de uno, muestra todos) y su descripcion.
6. Salir '''

print(menu)

opcion = int(input("\nIndica la opción elegida: "))
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
    if opcion == 6:
        print("Salir del programa")  
        print()

    print(menu)
    opcion = int(input("\nIndica la opción elegida: "))
    
    print()
