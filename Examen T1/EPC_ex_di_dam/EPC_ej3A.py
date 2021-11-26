
print("EJERCICIO 3")

lista=[]
opcion=1
while(opcion!=9):
    while True:
        try:
            opcion=int(input('''\nEscoge una de las opciones:
            \t1.-Añadir número.
            \t2.-Añadir número a la lista en una posición.
            \t3.-Longitud de la lista.
            \t4.-Eliminar el último número.
            \t5.-Eliminar un número.
            \t6.-Contar apariciones.
            \t7.-Posiciones de un número.
            \t8.-Mostrar números.
            \t9.-Salir.\n'''))
            break
        except ValueError:
            print("ERROR.Debes introducir un número.")
    if(opcion==1):
        print("AÑADIR UN NÚMERO")
        while True:
            try:
                num=float(input("Número:"))
                lista.append(num)
                break
            except ValueError:
                print("ERROR. Debes introducir un número.")
    elif(opcion==2):
        print("AÑADIR UN NÚMERO EN UNA POSICIÓN DETERMINADA")
        while True:
            try:
                num=float(input("Número:"))
                break
            except ValueError:
                print("ERROR. Debes introducir un número.")

        pos=0
        while(pos>(len(lista)+1) or pos<1):  
            while True:
                try:         
                    pos=int(input("Posición:"))
                    break
                except ValueError:
                    print("ERROR. Debes introducir un número.")
            if(pos>(len(lista)+1) or pos<1):
                print("No existe esa posición en la lista.")
            else:
                lista.insert(pos-1,num)     
    elif(opcion==3):
        print("LONGITUD DE LA LISTA")
        print("Número de elementos en la lista:",len(lista))
    elif(opcion==4):
        print("ELIMINAR EL ÚLTIMO NÚMERO")
        if(len(lista)>0):
            print(lista.pop(),"ha sido eleminado.")
        else:
            print("No hay elementos para eliminar.")
    elif(opcion==5):
        print("ELIMINAR UN NÚMERO DADA UNA PSOSIÓN")
        pos=0
        while(pos>(len(lista)+1) or pos<1):  
            while True:
                try:         
                    pos=int(input("Posición:"))
                    break
                except ValueError:
                    print("ERROR. Debes introducir un número.")
            if(pos>(len(lista)+1) or pos<1):
                print("No existe esa posición en la lista.")
            else:
                lista.pop(pos-1)
    elif(opcion==6):
        print("CONTAR APARICIONES")
        while True:
            try:
                num=float(input("Número:"))
                break
            except ValueError:
                print("ERROR. Debes introducir un número.")
        print(num,"se repite",lista.count(num),"veces.")
    elif(opcion==7):
        print("POSICIONES DE UN NÚMERO")
        while True:
            try:
                num=float(input("Número:"))
                break
            except ValueError:
                print("ERROR. Debes introducir un número.")
        
        posiciones=[]
        i=0
        while(i<len(lista)):
            try:
                if(lista.index(num,i)+1 not in posiciones):
                    posiciones.append(lista.index(num,i)+1)
            except ValueError:
                print(num,"no está en la lista.")
            i=i+1
        print("Pociones:",posiciones)
    elif(opcion==8):
        print("LISTA DE NÚMEROS")
        print(lista)
