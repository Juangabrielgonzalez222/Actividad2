
class  ViajeroFrecuente:
    __numeroviaj=0
    __DNI=""
    __nombre=""
    __apellido=""
    __millas=0
    def __init__(self,numero=None,dni=None,nombre=None,apellido=None,millas=None):
        if((type(numero)==int)and(type(dni)==str)and(type(nombre)==str)and(type(apellido)==str)and(type(millas)==int)):
            self.__numeroviaj=numero
            self.__DNI=dni
            self.__nombre=nombre
            self.__apellido=apellido
            self.__millas=millas
        else:
            print("error en el tipo de algún dato, no se guardo correctamente al viajero")
    def cantidadTotaldeMillas(self):
        return self.__millas
    def acumularMillas(self,nuevasMillas):
        if(type(nuevasMillas)==int):
            self.__millas+=nuevasMillas
            print("cantidad nueva de millas:",self.__millas)
        else:
            print("No se pudo realizar la operacion, tipo incorrecto de dato")
    def canjearMillas(self,cantMillas):
        if(type(cantMillas)==int):
            if(cantMillas>self.__millas):
                print("Error,la cantidad solicitada es mayor que la que tiene el viajero: ",self.__millas )
            else:
                self.__millas-=cantMillas
                print("La cantidad de millas restantes es: ",self.__millas)
        else:
            print("No se pudo realizar la operacion, tipo incorrecto de dato")
    def test(self):
        prueba1=ViajeroFrecuente(19,"33442121","Joaquin Manuel","Fernandez",5244)
        prueba2=ViajeroFrecuente("20","37123284","Tobias","Castro","5674")
        prueba3=ViajeroFrecuente()
        prueba4=ViajeroFrecuente(13,"42098563","Martin")
        print(prueba1.cantidadTotaldeMillas())
        print(prueba2.cantidadTotaldeMillas())
        print(prueba4.cantidadTotaldeMillas())
        prueba1.acumularMillas(200)
        prueba3.acumularMillas(100)
        prueba1.acumularMillas("200")
        prueba1.canjearMillas(100000)
        prueba1.canjearMillas("100")
            