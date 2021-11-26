
print("EJERCICIO 2")

limMenor=1
limMayor=0
while(limMayor<limMenor):
    while True:
        try:
            limMenor=float(input("\nIntroduce el límite INFERIOR del intervalo:"))
            break
        except ValueError:
            print("ERROR.Debe introducir un número.")

    while True:
        try:
            limMayor=float(input("\nIntroduce el límite SUPERIOR del intervalo:"))
            if(limMayor<limMenor):
                print("ERROR.El límite superior debe ser mayor que límite inferior.")
            break
        except ValueError:
            print("ERROR.Debe introducir un número.")    


print("\nIntroduce todos los números que quieras, cuando no quieras introdicir más, introduce un cero.")

num=1
lista=[]
while(num!=0):
    while True:
        try:
            num=float(input("Número: "))
            if(num!=0):
                lista.append(num)
            break
        except ValueError:
            print("Debes introducir sólo números.")

suma=0
for a in lista:
    if(a>limMenor and a<limMayor):
        suma=suma+a

contador=0
for a in lista:
    if(a<=limMenor or a>=limMayor):
        contador=contador+1

numeroIgualAlLimite=False
for a in lista:
    if(a==limMenor or a==limMayor):
        numeroIgualAlLimite=True

if(numeroIgualAlLimite):
    igual="SÍ"
else:
    igual="NO"

print("\nIntervalo (",limMenor,",",limMayor,")")
print("Números",lista)
print("SUMA de los números dentro del intervalo:",suma)
print("Números fuera del intervalo:",contador)
print("Números coincidentes con los límites: "+igual)

