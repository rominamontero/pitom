# crear un gestor de peliculas
# EL titulo debe tener mas de 2 caracteres
# el año debe ser mayor a 1960 y debe der menor al año actual
# El director debe tener nombre y apellido
# mostar el sigueinte menú
# '''1.- ingresar Pelicula
# 2.- quitar Pelicula
# 3.- Actualizar Pelicula
# 4.- Mostar Peliculas
# 5.- Mostrar solo los titulos
# 6.- Mostrar los años de las peliculas ordenados
# 7.- Mostrar meplicula mejor calificada
# 8.- Salir
# '''
import time
from datetime import datetime

año_actual=datetime.now().year
peliculas=[]

def pedir_titulo():
    while True:
        titulo=input("Ingrese el titulo de la pelicula: ")
        if len(titulo)<=2:
            print("El titulo debe contener mas de 2 caracteres")
        else:
            return titulo
def pedir_año():
    while True:
        try:
            año=int(input("Ingrese el año de lanzamiento de la pelicula: "))
            if año <=1960:
                print("El año debe ser mayor a 1960")
            elif año >año_actual:
                print(f"No puede ser mayor que el año actual")
            else:
                return año
        except ValueError:
            print("Debe ingresar un valor numerico")
def pedir_director():
    while True:
        director=input("Ingrese el nombre y apellido del director: ")
        partes=director.split()
        if director=="":
            print("El director no puede estar vacio")
        elif len(partes) <2:
            print("Debe ingresar nombre y apellido")
        elif any(caracter.isdigit() for caracter in director):
            print("El nombre no puede contener numeros")
        else:
            return director
def pedir_calificacion():
    while True:
        try:
            calificacion=float(input("Ingrese la calificacion de la pelicula (1-10): "))
            if calificacion <1 or calificacion>10:
                print("La calificacion debe estar entre 1 y 10")
            else:
                return calificacion
        except ValueError:
            print("Debe ingresar un valor numerico")

def mostrar_menu():
    print("""
GESTOR DE PELICULAS
 1.- Ingresar pelicula
 2.- Quitar pelicula
 3.- Actualizar pelicula
 4.- Mostar peliculas
 5.- Mostrar solo los titulos
 6.- Mostrar los años de las peliculas ordenados
 7.- Mostrar pelicula mejor calificada
 8.- Salir""")
def ingresar_pelicula(peliculas):
    print("INGRESAR PELICULA")
    titulo=pedir_titulo()
    año=pedir_año()
    director=pedir_director()
    calificacion=pedir_calificacion()
    pelicula={"titulo": titulo,
              "año": año,
              "director": director,
              "calificacion":calificacion}
    peliculas.append(pelicula)
    time.sleep(0.5)
    print("pelicula ingresada correctamente")
def quitar_pelicula(peliculas):
    if len(peliculas)==0:
        print("No hay peliculas que quitar")
        return
    mostrar_peliculas(peliculas)
    try:
        op=int(input("Seleccione la pelicula que desea eliminar: "))
        if op <1 or op >len(peliculas):
            print("Numero de pelicula no valido")
        else:
            pelicula_eliminada=peliculas.pop(op-1)
        time.sleep(0.5)
        print("Pelicula eliminada correctamente")
        print(f"Pelicula eliminada: {pelicula_eliminada['titulo']}")
    except ValueError:
        print("Debe ingresar un valor numerico")
def actualizar_pelicula(peliculas):
    if len(peliculas)==0:
        print("No hay peliculas para actualizar")
        return
    mostrar_peliculas(peliculas)
    try:
        op=int(input("Seleccione la pelicula que desea actualizar: "))
        if op <1 or op>len(peliculas):
            print("Numero de pelicula no valido")
            return
        pelicula=peliculas[op-1]
        print("""
Seleccione le dato que desea actualizar
1.- Titulo
2.- Año
3.- Director
4.- Calificacion""")
        op2=int(input("Seleccione una opccion: "))
        match op2:
            case 1:
                pelicula["titulo"]=pedir_titulo()
            case 2:
                pelicula["año"]=pedir_año()
            case 3:
                pelicula["director"]=pedir_director()
            case 4:
                pelicula["calificacion"]=pedir_calificacion()
            case _:
                print("Opccion no valida")
        print("Pelicula actualizada correctamente")
    except ValueError:
        print("Debe ingresar un valor numerico")
def mostrar_peliculas(peliculas):
    print("LISTA DE PELICULAS")
    if len(peliculas)==0:
        print("No hay peliculas ingresadas para mostrar")
    else:
        for i in range(len(peliculas)):
            print(f"""
{i+1}.- {peliculas[i]['titulo']}
Año: {peliculas[i]['año']}
Director: {peliculas[i]['director']}
Calificacion: {peliculas[i]['calificacion']}""")
def mostrar_titulos(peliculas):
    if len(peliculas)==0:
        print("No hay peliculas ingresadas para mostrar")
    else:
        print("TITULOS DE PELICULAS")
        for pelicula in peliculas:
            print(f"- {pelicula['titulo']}")
def mostrar_años_ordenados(peliculas):
    if len(peliculas)==0:
        print("No hay peliculas ingresadas para mostrar")
        return
    años=[]
    for pelicula in peliculas:
        años.append(pelicula["año"])
    años.sort()
    print("AÑOS DE PELICULAS ORDENADOS")
    for año in años:
        print(año)
def mostrar_mejor_calificada(peliculas):
    if len(peliculas) == 0:
        print("No hay películas registradas.")
        return
    mejor=peliculas[0]
    for pelicula in peliculas:
        if pelicula["calificacion"] >mejor["calificacion"]:
            mejor=pelicula
    print("PELICULA MEJOR CALIFICADA")
    print(f"""
Titulo: {mejor["titulo"]}
Año: {mejor["año"]}
Director: {mejor["director"]}
Calificacion: {mejor["calificacion"]}""")

while True:
    mostrar_menu()
    try:
        op=int(input("Seleccione una opccion: "))
        match op:
            case 1:
                ingresar_pelicula(peliculas)
            case 2:
                quitar_pelicula(peliculas)
            case 3:
                actualizar_pelicula(peliculas)
            case 4:
                mostrar_peliculas(peliculas)
            case 5:
                mostrar_titulos(peliculas)
            case 6:
                mostrar_años_ordenados(peliculas)
            case 7:
                mostrar_mejor_calificada(peliculas)
            case 8:
                print("Saliendo...")
                time.sleep(1)
                break
            case _:
                print("Opcion no valida")
    except ValueError:
        print("Debe ingresar una opcion numerica")

