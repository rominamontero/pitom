# Crear un gestor de pacientes
# pacientes=[
#     {"nombre": " Aquiles Baeza", "prevision": "Fonasa", 
#      "temperatura":34.6, "grave": False}
#Crear al gestor de pacientes en un centro medico
# Para poner el nombre se debe validar que no este vacio 
# y ademas tenga mas de 8 caracteres
# Para la prevision de salud solo exiten 3 posibles valores
# Fonasa, Isapre, o Fodesa
# Al ingresar un paciente, se debe poner la temperatura
# Crear una funcion que valide si esta grave o no
# Para que este grave debe tener mas de 39°
# Cada atencion vale $25.000
# Los despcuentos corresponden a 
# FOnasa 54%
# Isapre 27%
# Fodesa 12,5%
import time

pacientes=[]
valor_atencion= 25000
descuentos={
    "Fonasa": 0.54,
    "Isapre": 0.27,
    "Fodesa":0.125
}

def mostrar_menu():
    print("""
GESTOR DE PACEINTES
1.- Ingresar pacientes
2.- Mostrar pacinetes
3.- Contar pacientes graves
4.- Contar ganancias
5.- Salir
          """)
def validar_grave(temperatura):
    if temperatura > 39:
        return True
    else:
        return False
def calcular_pago(prevision):
    descuento=descuentos[prevision]
    pago=valor_atencion-(valor_atencion*descuento)
    return pago
def ingresar_paciente(pacientes):
    while True:
        nombre=input("Ingrese el nombre del paciente: ").strip()
        if nombre=="":
            print("Error.El nombre no puede estar vacio")
        elif len(nombre)<=8:
            print("Error. El nombre debe tener mas de 8 caracteres")
        elif any(caracter.isdigit()for caracter in nombre):
            print("El nombre no puede contener")
        else:
            break
    while True:
        print("""
PREVISION DE SALUD
              1.- Fonasa
              2.- Isapre
              3.- Fodesa""")
        op=input("Seleccione la prevision: ")
        if op=="1":
            prevision="Fonasa"
            break
        elif op=="2":
            prevision="Isapre"
            break
        elif op=="3":
            prevision="Fodesa"
            break
        else:
            print("Opcion no valida")
    while True:
        try:
            temperatura=float(input("Ingrese la temperatura del paciente: "))
            if temperatura<=0:
                print("La temperatura debe ser mayor a 0")
            else:
                break
        except ValueError:
            print("Debe ingresar solo numeros")
    grave=validar_grave(temperatura)
    pago=calcular_pago(prevision)
    paciente={"nombre":nombre,
              "prevision": prevision,
              "temperatura":temperatura,
              "grave": grave,
              "pago":pago}
    pacientes.append(paciente)
    time.sleep(1)
    print(f"""PACIENTE INGRESADO CORRECTAMENTE
Nombre: {nombre}
Prevision: {prevision}
Temperatura: {temperatura}
Grave: {grave}
Total a pagar: ${pago}""")
def mostrar_pacientes(pacientes):
    print("LISTA DE PACIENTES")
    if len(pacientes)==0:
        print("No hay pacientes ingresados")
    else:
        for paciente in pacientes:
            print(f"""Nombre: {paciente["nombre"]}
    Prevision: {paciente["prevision"]}
    Temperatura: {paciente["temperatura"]}
    Grave: {paciente["grave"]}
    Pago: ${paciente["pago"]}""")
def contar_graves(pacientes):
    graves=0
    no_graves=0
    for paciente in pacientes:
        if paciente["grave"]==True:
            graves+=1
        else:
            no_graves+=1
    print(f"""Pacientes graves: {graves}
Pacientes no graves: {no_graves}""")
def contar_ganancias(pacientes):
    ganancias=0
    for paciente in pacientes:
        ganancias+=paciente["pago"]
    print(f"Ganancias: ${ganancias}")

while True:
    mostrar_menu()
    try:
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                ingresar_paciente(pacientes)
            case 2:
                mostrar_pacientes(pacientes)
            case 3:
                contar_graves(pacientes)
            case 4:
                contar_ganancias(pacientes)
            case 5:
                print("Saliendo...")
                time.sleep(1)
                break
            case _:
                print("Ingrese una opcion valida")
    except ValueError:
        print("Debe ingresar una opcion numerica")