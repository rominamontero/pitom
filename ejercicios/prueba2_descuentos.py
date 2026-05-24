medicamentos=60000
despacho=8000

edad=int(input("Ingrese su edad: "))
tramo=input("Ingrese su tramo (A, B, C o D): ").upper()

if tramo == "A" or tramo == "B":
    despacho=despacho-(despacho*0.10)
    if edad <= 30:
            medicamentos=medicamentos-(medicamentos*0.18)
    elif edad <= 31 or edad <= 60: 
            medicamentos=medicamentos-(medicamentos*0.12)
    if edad >= 55:
            despacho=despacho-(despacho*0.05)

if tramo == "C" or tramo == "D":
    if edad <= 30:
            medicamentos=medicamentos-(medicamentos*0.12)
    elif edad <= 31 or edad <= 60: 
            medicamentos=medicamentos-(medicamentos*0.08)
    if edad >= 55:
            despacho=despacho-(despacho*0.05)
print(f'''El valor de medicamentos es: {medicamentos}
El valor del despacho es: {despacho}''')                
