import random


aprobados=0
reprobados=0
total_estudiantes=0
promedio=0
calificaciones=0
porcentaje=0

saldo=100
total_jugadas=0
total_apuestas=0




print('''MENU
      1.- Registrar calificaciones
      2.- Jugar dados (apuestas)
      3.- Ver estadisticas completas
      4.- Buscar estudiante destacado
      5.- Salir''')
op=int(input("Sleccione una opccion: "))

while op != 5:
    match op:
        case 1:
            print("Registrar calificaciones")
            cant_estudiantes=int(input("Cuantos estudiantes va a registrar?: "))
            while cant_estudiantes<=0:
                print("Se debe ingresar como minimo un (1) estudiante")
                cant_estudiantes=int(input("Cuantos estudiantes va a registrar?: "))
            for i in range(cant_estudiantes):
                print(f"Estudiante {i+1}")
                nota=int(input("Ingrese una nota entre 0 y 100: "))
                while nota <0:
                    print("La nota debe estar entre 0 y 100")
                    nota=int(input("INgrese una nota entre 0 y 100: "))
                if nota >=60:
                    print("Estudiante aprobado")
                    aprobados+=1
                else:
                    print("Estudiante reprobado")
                    reprobados+=1
                total_estudiantes+=1
                calificaciones+=nota
                promedio=(calificaciones/cant_estudiantes)
                porcentaje=(aprobados/cant_estudiantes)*100
            print(f'''RESUMEN
                  Cantidad de estudiantes registrados en esta sesion: {total_estudiantes}
Suma de calificaciones: {calificaciones}
Promedio: {promedio}
Aprobados: {aprobados}
Reprobados: {reprobados}
Porcentaje aprobados: {porcentaje}''')
            print('''MENU
            1.- Registrar calificaciones
            2.- Jugar dados (apuestas)
            3.- Ver estadisticas completas
            4.- Buscar estudiante destacado
            5.- Salir''')
            op=int(input("Seleccione una opccion: "))            
        case 2:
            volver_a_jugar=1
            print("Jugar dados (apuestas)")
            print(f"Saldo total: {saldo}")
            while saldo>0 and volver_a_jugar==1:
                apuesta=int(input("Cuanto quiere apostar: "))
                while apuesta<0 or apuesta>saldo:
                    print("La apuesta debe ser mayor que 0 o igual a su saldo")
                    apuesta=int(input("Cuanto quiere apostar: "))
                dado1=random.randint(1,6)
                dado2=random.randint(1,6)
                suma_dados=dado1+dado2
                if suma_dados==7 or suma_dados==11:
                    print("Ganaste el doble de lo apostado")
                    saldo=saldo+(apuesta*2)
                elif suma_dados==2 or suma_dados==3 or suma_dados==12:
                    print("Perdiste todo")
                    saldo=saldo-apuesta
                else:
                    dado3=random.randint(1,6)
                    if dado3 >=4:
                        print("Ganste")
                        saldo=saldo+(apuesta*1.5)
                    else:
                        print("Perdiste todo todito")
                        saldo-=apuesta
                print(f"Tu saldo actual es: {saldo}")
                volver_a_jugar=int(input('''Quieres volver a jugar (si/no)
                                     1.- SI
                                     2.- NO 
                                         '''))
                while volver_a_jugar !=1 and volver_a_jugar!=2:
                    print("Opcion invalida")
                    volver_a_jugar=int(input('''Quieres volver a jugar (si/no)
                                     1.- SI
                                     2.- NO 
                                         '''))
                if volver_a_jugar ==2:
                    break
            print('''MENU
      1.- Registrar calificaciones
      2.- Jugar dados (apuestas)
      3.- Ver estadisticas completas
      4.- Buscar estudiante destacado
      5.- Salir''')
            op=int(input("Seleccione una opccion: "))





                

        case 3:
            print("Ver estadisticas completas")
        case 4:
            print("uscar estudiante destacado")
        case 5:
            print("Salir")
        case _:
            print("Opcion invalida")