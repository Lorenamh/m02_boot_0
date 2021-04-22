#El nombre va con la primera con mayusculas por convencion.
#Los objetos se pueden modificar, por ejemplo defino un Perro, y
#después lo modifico
class Perro():
    #Siempre empieza con la función constructor, es lo que nos permite crear la instancia
    def __init__(self,nombre,edad,peso):
        self.nombre= nombre
        self.edad=edad
        self.peso=peso
    #El primer parametros de la función es la propia clase    
    def ladrar(self,c):#Siempre hay que introducirlo
        if self.peso >= 8:
            print("GUAU, GUAU",c)
        else:
            print("guau, guau",c)  
#salchicho = Perro('Salchicho',3,12)
#salchicho.ladrar("cadena")
    def __str__(self): #Para que cuando llame a mi objeto no me salga una cosa fea
        return "Soy el perro {}".format(self.nombre)
    
    
class PerroAsistencia(Perro):
    #COmo vemos en lugar de dejarlo vacio pongo la clase de la que hereda
    def __init__(self,nombre,edad,peso,amo):
        Perro.__init__(self,nombre,edad,peso)
        self.amo=amo
        self.__trabajando=False
    def __str__(self):
            return "Perro de asistencia de {}".format (self.amo)
        
    def pasear(self):
        print("{} ayudo a mi dueño, {} a pasear".format(self.nombre,self.amo))
    def ladrar(self):
        if self.__trabajando:
            print( " shhhh, no puedo ladrar")
        else:
            Perro.ladrar(self,c)
    def trabajando (self,valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando=valor