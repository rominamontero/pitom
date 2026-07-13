#Gestor de peliculas y prestamos

peliculas={
    "P001": ["Interestelar", "Christopher Nolan", 2014, 5],
    "P002": ["Titanic", "James Cameron", 1997, 4],
    "P003": ["Dune", "Denis Villeneuve", 2021, 5],
    "P004": ["Como entrenar a tu dragon", "Chris Sanders", 2010, 4]

}
prestamos={
    "P001": ["10-07-2026", "DISPONIBLE"],    
    "P002": ["06-07-2026", "PRESTADA"],
    "P003": ["20-06-2026", "DISPONIBLE"],
    "P004": ["27-06-2026", "PRESTADA"]

}

#Validaciones

def validar_codigo(codigo):
    codigo=codigo.strip().upper()
    if codigo.strip() == "":
        return False
    if not codigo.startswith("P"):
        return False
    if len(codigo) != 4:
        return False
    if codigo in peliculas:
        return False
    if not codigo[1:].isdigit():
        return False
    else:
        return True
    
def validar_titulo(titulo):
    titulo=titulo.strip()
    if titulo == "":
        return False
    if len(titulo) <2:
        return False
    else:
        return True

def validar_director(director):
    partes=director.split()
    if len(partes) <2:
        return False
    if director.strip() == "":
        return False
    else:
        return True

def validar_estreno(fecha_estreno):
    try:
        fecha_estreno=int(fecha_estreno)
        if fecha_estreno <1960:
            return False
        if fecha_estreno > 2026:
            return False
    except ValueError:
        return False
    return True

def validar_calificacion(calificacion):
    try:
        calificacion=int(calificacion)
        if calificacion <1 or calificacion >5:
            return False
    except ValueError:
        return False
    return True

def validar_fecha_ingreso(fecha_ingreso):
    if fecha_ingreso.strip() == "":
        return False
    else: 
        return True
    
def validar_buscar_anio(anio_min, anio_max):
    try:
        anio_min=int(anio_min)
        anio_max=int(anio_max)
        if anio_min <1960 or anio_min >2026:
            return False
        if anio_max >2026 or anio_max <1960:
            return False
        if anio_min > anio_max:
            return False
        return True
    except ValueError:
        return False

#Funciones

def mostrar_menu():
    print("""
1. Ingresar película
2. Buscar película por código
3. Mostrar todas las películas
4. Contar películas por director
5. Buscar películas por rango de años
6. Actualizar estado de una película
7. Eliminar película
8. Mostrar película mejor calificada
9. Salir""")    

def pedir_pelicula():
    codigo=input("Ingrese el codigo de la pelicula (EJ: P000): ").strip().upper()
    titulo=input("Ingrese el titulo de la pelicula: ").strip()
    director=input("Ingrese el director de la pelicula: ").strip()
    fecha_estreno=input("Ingrese la fecha de estreno de la pelicula: ")
    calificacion=input("Ingrese la calificacion de la pelicula: ")
    fecha_ingreso=input("Ingrese la fecha de ingreso: ").strip()
    ingresar_pelicula(codigo, titulo, director, fecha_estreno, calificacion, fecha_ingreso)
    
def ingresar_pelicula(codigo, titulo, director, fecha_estreno, calificacion, fecha_ingreso):
    if validar_codigo(codigo) == False:
        print("Debe ingresar el codigo con el formato presentado")
        return
    if validar_director(director) == False:
        print("El director no puede estar vacio y debe contar con nombre y apellido")
        return
    if validar_titulo(titulo) == False:
        print("El tituo no debe estar vacio y debe tenr al menos 2 caracteres")
        return
    if validar_estreno(fecha_estreno) == False:
        print("La fecha de estreno debe etar entre 1960 y 2026")
        return
    if validar_calificacion(calificacion) == False:
        print("La calificacion debe estar entre 1 y 5")
        return
    if validar_fecha_ingreso(fecha_ingreso) == False:
        print("La fehca de ingreso no puede estar vacia")
        return
    
    fecha_estreno=int(fecha_estreno)
    calificacion=int(calificacion)
    peliculas[codigo]= [titulo, director, fecha_estreno, calificacion]
    prestamos[codigo]=[fecha_ingreso, "DISPONIBLE"]

    print("Pelicula ingresada correctamente")

def buscar_por_codigo():
    codigo=input("Ingrese el codigo a buscar: ")
    codigo=codigo.strip().upper()
    
    if codigo in peliculas:
        titulo=peliculas[codigo][0]
        director=peliculas[codigo][1]
        fecha_estreno=peliculas[codigo][2]
        calificacion=peliculas[codigo][3]
        fecha_ingreso=prestamos[codigo][0]
        estado=prestamos[codigo][1]
        print(f"""
Codigo: {codigo}
Titulo: {titulo}
Director: {director}
Año: {fecha_estreno}
Calificacion: {calificacion}
Fecha de ingreso: {fecha_ingreso}
Estado: {estado}
""")
    else:
        print("El codigo no exite")

def contar_director():
    director_buscado=input("INgrese el nombre del director a buscar: ").lower().strip()
    total=0
    for codigo in peliculas:
        director_pelicula=peliculas[codigo][1].lower()
        if director_buscado == director_pelicula:
            total+=1
    if total > 0:
        print(f"Total de peliculas encontradas: {total}")
    else:
        print("No se encontraron peliculas")

def buscar_anio():
    anio_min=input("Ingrese el año minimo: ")
    anio_max=input("Ingrese el año maximo: ")
    if validar_buscar_anio(anio_min, anio_max)==False:
        print("El rango de años no es valido")
        return
    anio_min=int(anio_min)
    anio_max=int(anio_max)

    encontrados=0
    for codigo in peliculas:
        anio=peliculas[codigo][2]
        if anio_min <= anio <= anio_max:
            print(f"""
                Codigo: {codigo}
                Titulo: {peliculas[codigo][0]}
                Año: {anio}
                  """)
            encontrados+=1
    if encontrados == 0:
        print("No se encontraron peliculas dentro del rango")

def actualizar_estado():
    codigo=input("Ingrese el codigo de la pelicula: ").strip().upper()
    
    if codigo not in prestamos:
        print("El codigo no existe")
        return 
    while True:
        print("""Seleccione el nuevo estado
              1.- Disponible
              2.- Prestada""")
        op=input("Seleccione una opcion: ").strip()
        match op:
            case "1":
                prestamos[codigo][1]="DISPONIBLE"
                break
            case "2":
                prestamos[codigo][1]="PRESTADA"
                break
            case _:
                print("Opcion no valida")
        
    print(f"Estado actializado a: {prestamos[codigo][1]}")

def eliminar_pelicula():
    codigo = input("Ingrese el código de la película: ").strip().upper()

    if codigo not in peliculas:
        print("El código no existe")
        return

    if prestamos[codigo][1] == "PRESTADA":
        print("No se puede eliminar porque la película está prestada")
        return

    peliculas.pop(codigo)
    prestamos.pop(codigo)

    print("Película eliminada correctamente")

def mejor_calificada():
    if len(peliculas)==0:
        print("Nohay peliculas que mostrar")
        return
    mejor=0
    for codigo in peliculas:
        calificacion=peliculas[codigo][3]
        if calificacion > mejor:
            mejor = calificacion
    for codigo in peliculas:
        calificacion = peliculas[codigo][3]
        if calificacion == mejor:
            titulo=peliculas[codigo][0]
            director=peliculas[codigo][1]
            print(f"""
Código: {codigo}
Título: {titulo}
Director: {director}
Calificación: {calificacion}
""")
            
def mostrar_peliculas():
    if len(peliculas)==0:
        print("No hay peliculas que mostrar")
        return
    for codigo in peliculas:
        titulo=peliculas[codigo][0]
        director=peliculas[codigo][1]
        fecha_estreno=peliculas[codigo][2]
        calificacion=peliculas[codigo][3]
        fecha_ingreso=prestamos[codigo][0]
        estado=prestamos[codigo][1]
        print(f"""
Codigo: {codigo}
Titulo: {titulo}
Director: {director}
Año: {fecha_estreno}
Calificacion: {calificacion}
Fecha de ingreso: {fecha_ingreso}
Estado: {estado}
""")



while True:
    mostrar_menu()
    try:
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                pedir_pelicula()
            case 2:
                buscar_por_codigo()
            case 3:
                mostrar_peliculas()
            case 4:
                contar_director()
            case 5:
                buscar_anio()
            case 6:
                actualizar_estado()
            case 7:
                eliminar_pelicula()
            case 8:
                mejor_calificada()
            case 9:
                print("saliendo...")
                break
            case _:
                print("Opcion no valida")

    except ValueError:
        print("Debe ingresar una opcion numerica")