import csv
from clase import ViajeroFrecuente
if __name__=='__main__':
    lista=[]
    bandera=0
    n=None
    archivo=open("viajeros.csv")
    reader=csv.reader(archivo,delimiter=";")
    for fila in reader:
        if(bandera==0):
            bandera=1
        else:
            lista.append(ViajeroFrecuente(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4])))
    archivo.close()        
    numero=int(input("Ingresa el numero de viajero a utilizar:")) 
    while(numero > len(lista)):
        print("El numero ingresado es mayor que la cantidad de viajeros: ",len(lista))
        numero=int(input("Vuelva a ingresar el numero de viajero:"))
    numero-=1
    while(n!=4):
        print("Menu:")
        print("Ingresa 1 para consultar las millas")
        print("Ingresa 2 para acumular millas")
        print("Ingresa 3 para canjear millas")
        print("Ingresa 4 para salir")
        n=int(input("Ingresa número de opción: "))
        if(n==1):
            print("Cantidad de millas:",lista[numero].cantidadTotaldeMillas())
        elif(n==2):
            millas=int(input("Ingresa la cantidad de millas a acumular: "))
            lista[numero].acumularMillas(millas)
        elif(n==3):
            millas=int(input("Ingresa la cantidad de millas a canjear: "))
            lista[numero].canjearMillas(millas)
    print("funcion de testeo:")
    lista[numero].test()
    

       