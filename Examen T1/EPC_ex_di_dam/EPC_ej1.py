
print("EJERCICIO 1")

cadena=str(input("\nIntroduce una cadena: "))

car1=""
car2=""
while(len(car1)!=1):
    car1=str(input("Introduce un carácter:"))
    if(len(car1)!=1):
        print("No has introducido un carácter.")

while(len(car2)!=1):
    car2=str(input("Introduce otro carácter:"))
    if(len(car2)!=1):
        print("No has introducido un carácter.")

nuevaCadena=""
for c in cadena:
    if(car1==c):
        c=car2
    nuevaCadena=nuevaCadena+c

print(nuevaCadena)


