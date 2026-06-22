# crear un gestor de estacionamiento
# Un estacionamiento tiene 4 pisos
# y cada piso tiene 20 espacios
#  Preguntar cuando entra un vehiculo, que tipo de vheiculo es
# vehículo ligero 2000
# vehículo mediano 3000
# vehículo pesado 3500

# luego , acomodarlo en algun lugar de algun piso disponible.
# el menu dsebe tener las sigueintes alternativas

# ''' 1.- ingresar vehiculo
# 2.- contar ganancias
# 3.- contar vehiculos'''

# usa lista o diccionario segun le acomode mas
import time

tipo=""
pisos=4
espacios_por_piso=20
estacionamiento=[]
for piso in range(pisos):
    estacionamiento.append([None]*espacios_por_piso)
tarifas={
    "1":2000,
    "2":3000,
    "3":3500
}
tipos={
    "1":"Vehiculo ligero",
    "2":"Vehiculo mediano",
    "3":"Vehiculo pesado"
}
contador={
    "Vehiculo ligero":0,
    "Vehiculo mediano":0,
    "Vehiculo pesado":0,
}
ganancias=0




def mostrar_menu():
    print('''
          1.- Ingresar vehiculo
          2.- Contar ganancias
          3.- Contar vehiculos
          4.- Salir
          ''')  
def ingresar_vehiculo(estacionamiento, tarifas, tipos, contador, ganancias):
    while True:
        print("""
    TIPOS DE VEHICULOS
    1.- Vehiculo ligero $2000
    2.- Vehiculo mediano $3000
    3.- Vehiculo pesado $3500
            """)
        tipo=input("Seleccione el tipo de vehiculo: ")
        
        if tipo in tipos:
            break
        else:
            print("Error. Tipo de vehiculo no valido, intente nuevamente")
            
    for piso in range(len(estacionamiento)):
        for espacio in range(len(estacionamiento[piso])):
            if estacionamiento[piso][espacio] == None:
                estacionamiento[piso][espacio] = tipos[tipo]
                ganancias+=tarifas[tipo]
                contador[tipos[tipo]]+=1
                print(f"""
Vehiculo ingresado correctamente
Ubicacion: Piso {piso+1}, espacio {espacio+1}
Valor cobrado: ${tarifas[tipo]}""")
                return ganancias
    print("No hay espacios disponibles")
    return ganancias
def contar_ganancias(ganancias):
    print(f"""
GANANCIAS
Ganancias totales: ${ganancias}""")
def contar_vehiculos(contador, estacionamiento):
    for vehiculo in contador:
        print(f"{vehiculo}:{contador[vehiculo]}")
    espacios_disponibles=0
    for piso in range(len(estacionamiento)):
        for espacio in range(len(estacionamiento[piso])):
            if estacionamiento[piso][espacio]==None:
                espacios_disponibles+=1

#MENU DE RIAL
while True:
    mostrar_menu()
    try:
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                ganancias=ingresar_vehiculo(estacionamiento, tarifas, tipos, contador, ganancias)
            case 2:
                contar_ganancias(ganancias)
            case 3:
                contar_vehiculos(contador, estacionamiento)
            case 4:
                print("Saliendo del programa...")
                time.sleep(1)
                break
            case _:
                print("Error. Opcion no valida")
    except ValueError:
        print("Solo debe ingresar una opcion numerica")