
autos={"A001":["Toyota", "Corolla", 2020, 5],
       "A002":["Kia", "Rio", 2019, 4],
       "A003":["Toyota", "Yaris", 2021, 3]}
operaciones={"A001":["10-01-2024", "15-03-2024"],
             "A002":["05-02-2014", "PENDIENTE"],
             "A003":["20-04-2024", "PENDIENTE"]}

#Validaciones

def validar_id(id_auto):
    if id_auto.strip() != "":
        return True
    else:
        return False
    
def validar_marca(marca):
    if marca.strip() != "":
        return True
    else:
        return False
    
def validar_modelo(modelo):
    if modelo.strip() != "":
        return True
    else:
        return False

def validar_anio(anio):
    try:
        anio=int(anio)
        if anio > 1900:
            return True
        else:
            return False
    except ValueError:
        return False
    
def validar_ranking(ranking):
    try:
        ranking=int(ranking)
        if ranking>=1 and ranking<=5:
            return True
        else:
            return False
    except ValueError:
        return False
    
def validar_fecha_ingreso(fecha_ingreso):
    if fecha_ingreso.strip() != "":
        return True
    else:
        return False

def validar_fecha_venta(fecha_venta):
    if fecha_venta.strip() != "":
        return True
    else:
        return False

#Funcioness

def autos_vendidos_por_marca(marca):
    total=0
    for id_auto in autos:
        datos_auto=autos[id_auto]
        marca_auto=datos_auto[0]
        if marca_auto.lower()==marca.lower():
            datos_operacion=operaciones[id_auto]
            fecha_venta = datos_operacion[1]

            if fecha_venta != "PENDIENTE":
                total+=1
    print(f"Total de autos vendidos de la marca {marca}: {total}")

def busqueda_por_anio(anio_min, anio_max):
    resultados=[]
    for id_auto in autos:
        marca=autos[id_auto][0]
        modelo=autos[id_auto][1]
        anio=autos[id_auto][2]
        fecha_venta=operaciones[id_auto][1]
        if anio >= anio_min and anio <= anio_max and fecha_venta == "PENDIENTE":
            texto=f"{marca} {modelo}--{id_auto}"
            resultados.append(texto)
    if len(resultados) == 0:
        print("No existen vehiculos disponibles")
    else:
        resultados.sort()
        print("Vehiculos encontados: ")
        for auto in resultados:
            print(auto)

def actualizar_fecha_venta(id_auto, nueva_fecha):
    if id_auto in operaciones:
        operaciones[id_auto][1]= nueva_fecha
        return True
    else:
        return False
    
def opcion_actualizar():
    while True:
        id_auto=input("Ingrese el ID del vehiculo: ").strip().upper()
        nueva_fecha=input("Ingrese nueva fecha de venta")
        resultado=actualizar_fecha_venta(id_auto, nueva_fecha)

        if resultado == True:
            print("Fecha de venta actualizada correctamente")
        else:
            print("El identificador no existe")
                    
        repetir=input("Desea actualizar otro vehiculo? (s/n): ").lower()
        if repetir != "s":
            break

def incorporar_auto(id_auto, marca, modelo, anio, ranking, fecha_ingreso, fecha_venta):
    if validar_id(id_auto)==False:
        print("El ID no puede estar vacio")
        return
    if id_auto in autos:
        print("El ID ya se enceuntra registrado")
        return
    if validar_marca(marca)==False:
        print("La marca no puede estar vacia")
        return
    if validar_modelo(modelo)==False:
        print("El modelo no puede estar vacio")
        return
    if validar_anio(anio)==False:
        print("El año debe ser mayor a 1900")
        return
    if validar_ranking(ranking)==False:
        print("El ranking debe ser un nuemro entero entre 1 y 5")
        return
    if validar_fecha_ingreso(fecha_ingreso)==False:
        print("La fecha de ingreso no puede estar vacia")
        return
    if validar_fecha_venta(fecha_venta)==False:
        print("La fecha de venta no puede estar vacia")
        return
    anio=int(anio)
    ranking=int(ranking)
    autos[id_auto]=[marca, modelo, anio, ranking]
    operaciones[id_auto]=[fecha_ingreso, fecha_venta]

    print("Vehiculo registrado correctamente")

def pedir_auto():
    id_auto=input("Ingrese ID del vehiculo: ").strip().upper()
    marca=input("Ingrese marca del vehiculo: ")
    modelo=input("Ingrese modelo del vehiculo: ")
    anio=input("Ingrese año del vehiculo: ")
    ranking=input("Ingrese ranking del 1 al 5 del vehiculo: ")
    fecha_ingreso=input("Ingrese fecha de ingreso del vehiculo: ")
    fecha_venta=input("Ingrese fecha de venta (o Pendiente) del vehiculo: ").upper()
    
    incorporar_auto(id_auto, marca, modelo, anio, ranking, fecha_ingreso, fecha_venta)

def eliminar_auto(id_auto):
    if id_auto in autos and id_auto in operaciones:
        del autos[id_auto]
        del operaciones[id_auto]
        return True
    else:
        return False
    
def pedir_eliminar_auto():
    id_auto=input("Ingrese le ID del vehiculo: ").strip().upper()
    resultado=eliminar_auto(id_auto)
                
    if resultado==True:
        print("Vehiculo eliminado")
    else:
        print("El identificador no existe")

def contar_autos_marca(marca):
    total=0
    for id_auto in autos:
        marca_auto=autos[id_auto][0]
        if marca_auto.lower() ==marca.lower():
            total+=1
    print(f"Total de autos de la marca {marca}: {total}")

while True:
    print("""
          MENU AUTOMOTORA
          1.- Autos vendidos por marca
          2.- Buscar vehiculos por año
          3.- Actualizar fecha de venta
          4.- Incorporar vehiculo nuevo
          5.- Eliminar vehiculo
          6.- Total de autos por marca
          7.- Salir """)
    try:
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                marca=input("Ingrese la marca que desea buscar: ")
                autos_vendidos_por_marca(marca)
            case 2:
                try:
                    anio_min=int(input("Ingrese el año minimo: "))
                    anio_max=int(input("Ingrese el año maximo: "))
                    busqueda_por_anio(anio_min, anio_max)
                except ValueError:
                    print("Debe ingresar años como numero")
            case 3:
                opcion_actualizar()
            case 4:
                pedir_auto()
            case 5:
                pedir_eliminar_auto()
            case 6:
                marca=input("Ingrese la marca que desea buscar: ")
                contar_autos_marca(marca)
            case 7:
                print("Saliendo del sistema...")
                break
            case _:
                print("Opcion no valida")
    except ValueError:
        print("Debe ingresar una opcion numerica")