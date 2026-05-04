

# if ptos >0 and ptos <=3:
#     print("Usted es un alumno de buen desempeño")
# elif ptos>=4 and ptos <=6:
#     print("Usted es un alumno que puede mejorar")
# elif ptos>=7 and ptos<=9:
#     print("Usted es un alumno con algunos desafios")
# else:
#     print("Usted es un alumno con muchos desafios")
ptos=0

p1=input("¿Deja para después lo que puede hacer ahora? (si/no)")
p2=input("¿Presta atención en clases? (si/no)")
p3=input("¿Resuelve sus dudas con el profesor? (si/no)")
p4=input("¿Prueba sus hipótesis antes de preguntar? (si/no)")
p5=input("¿Utiliza su tiempo libre para aprender cosas nuevas? (si/no)")
p6=input("¿Utiliza otra fuente de información para resolver dudas? (si/no)")
p7=input("¿Estudia solo un día antes de la prueba? (si/no)")
p8=input("¿A sus amigos solo les gusta pasar el rato? (si/no)")
p9=input("¿A menudo realiza acciones que no son importantes? (si/no)")
p10=input("¿Le gustaría no tener que trabajar? (si/no)")
p11=input("¿Le gusta leer? (si/no)")
p12=input("¿Le gustan las redes sociales? (si/no)")



if p1=="si":
    ptos+=1
if p2=="no":
    ptos+=1
if p3=="no":
    ptos+=1
if p4=="no":
    ptos+=1
if p5=="no":
    ptos+=1
if p6=="no":
    ptos+=1
if p7=="si":
    ptos+=1
if p8=="si":
    ptos+=1
if p9=="si":
    ptos+=1
if p10=="si":
    ptos+=0
if p11=="no":
    ptos+=1
if p12=="si":
    ptos+=1

if ptos >0 and ptos <=3:
    print("Usted es un alumno de buen desempeño")
elif ptos>=4 and ptos <=6:
    print("Usted es un alumno que puede mejorar")
elif ptos>=7 and ptos<=9:
    print("Usted es un alumno con algunos desafios")
else:
    print("Usted es un alumno con muchos desafios")