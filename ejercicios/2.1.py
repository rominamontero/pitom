import random
import time

op=0

ptos=0
nptos=0

seis=0
numda=0

puntajes=0
suma=0
cant=0
print(''' MENU PRINCIPAL
      1.- Adivinar numero
      2.- Lanzar dedos
      3.- Calcular promedio de puntajes
      4.- Ver estadisticas
      5.- Salir''')
op=int(input("Seleccione una opcion: "))

while op!=5:
    match op:
        case 1:
            print("Adivinar numero")
            adivinado=False
            intentos=3
            num=random.randint(1,10)
            print("Adivina el numero entre 1 y 10")
            for i in range(intentos):
                ad=int(input(f"Intento {i+1} de {intentos}: "))
                if ad == num:
                    print(f"Correcto el numero era {num}")
                    ptos+=1
                    adivinado=True
                    break
                elif ad < num:
                    print(f"Muy bajo.")
                elif ad > num:
                    print(f"Muy alto.")
            if not adivinado:
                nptos+=1
                print(f"Perdiste el numero era {num}")
            print(''' MENU PRINCIPAL
      1.- Adivinar numero
      2.- Lanzar dedos
      3.- Calcular promedio de puntajes
      4.- Ver estadisticas
      5.- Salir''')
            op=int(input("Seleccione una opcion: "))
        case 2:
            print("Lanzar dados")
            ld=int(input("Cuantas veces desea lanzar el dado: "))
            if ld<=0:
                print("El minimo de lanzamientos es 1")
                ld=int(input("Cuantas veces desea lanzar el dado: "))
                
            else:
                for i in range(ld):
                    dado=random.randint(1,6)
                    print(f"Lanzamiento {i+1}: {dado}")
                    if dado==6:
                        seis+=1
                    numda+=1
            print(''' MENU PRINCIPAL
      1.- Adivinar numero
      2.- Lanzar dedos
      3.- Calcular promedio de puntajes
      4.- Ver estadisticas
      5.- Salir''')
            op=int(input("Seleccione una opcion: "))
        case 3:
            suma=0
            sesenta=0
            print("Calcular puntaje")
            cant=int(input("Cuantos puntajes quiere ingresar: "))
            while cant<=0:
                print("Debe ingresar como minimo un (1) puntaje")
                cant=int(input("Cuantos puntajes quiere ingresar: "))
            for s in range(cant):
                puntajes=int(input(f"Ingrese el puntaje {s+1}: "))
                while puntajes <=0 or puntajes >100:
                    print("EL puntaje debe estar entre 1 y 100")
                    puntajes=int(input(f"Ingrese el puntaje {s+1}: "))
                suma+=puntajes
                if puntajes >= 60:
                    sesenta+=1
            print(f"La suma total de sus puntajes es de: {suma}")
            print(f"El promedio de sus {cant} puntajes es {suma/cant}")
            print(f"{sesenta} Jugadores han aprobado")
            print(''' MENU PRINCIPAL
      1.- Adivinar numero
      2.- Lanzar dedos
      3.- Calcular promedio de puntajes
      4.- Ver estadisticas
      5.- Salir''')
            op=int(input("Seleccione una opcion: "))
        case 4:
            print("Ver estadisticas")
            print(f"Partidas ganadas en avivinar el numero: {ptos}")
            print(f"Partidas perdidas en adivinar el numero {nptos}")
            print(f"Total de dados lanzados: {numda}")
            print(f"Cantidad de veces que salio 6: {seis}")
            print(f"Suma total de puntajes ingresados: {suma}")
            print(f"Cantidad total de puntajes ingresados: {cant}")
            print(''' MENU PRINCIPAL
      1.- Adivinar numero
      2.- Lanzar dedos
      3.- Calcular promedio de puntajes
      4.- Ver estadisticas
      5.- Salir''')
            op=int(input("Seleccione una opcion: "))
        case _: 
            print("Opcion invalida")
            print(''' MENU PRINCIPAL
      1.- Adivinar numero
      2.- Lanzar dedos
      3.- Calcular promedio de puntajes
      4.- Ver estadisticas
      5.- Salir''')

            op=int(input("Seleccione una opcion: "))

print("Saliendo")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("Hasta luego. Gracias por usar el programa!")