
#Clase Principal y Abstracta 
class Figuras:
    def __init__(self,x,y,visible):
       self.x=x
       self.y=y
       self.visible=visible 

    def getX(self):
       return self.x

    def getY(self):
        return self.y

    def estaVisible(self):
        return self.visible

    def mostrar(self):
        print (f"La figura se esta mostrando")

    def ocultar(self):
        print (f"La figura se esta ocultando")

    def mover(self,x,y):
        print(f"La fugura se mueve en la siguiente coordenada: {self.getX(),self.getY()}")

    #Metodos de gettes y Setters faltantes

    def setX(self,x):
        self.x=x

    def setY(self,y):
        self.y=y

    def setVisible(self,visible):
        self.visible=visible


#Clases Scuendiarias
#Rectangulo

class Rectangulos(Figuras):
    def __init__(self,x,y,visible,alto,ancho):
        super().__init__(x,y,visible)
        self.alto=alto
        self.ancho=ancho

    def mostrar(self):
        print(f"El Rectangulo se encuentra visible: {self.estaVisible()} y se esta localizado en coordenada X,Y {self.getX(),self.getY()}, ademas tiene un alto y ancho de: {self.getAlto(), self.getAncho()} ")    

    def ocultar(self):
        print(f"El Rectangulo se esta ocultando")    
    
    #Resto de los metodos set y get 
    def getAlto(self):
        return self.alto

    def getAncho(self):
        return self.ancho

    def setAlto(self,alto):
        self.alto=alto

    def setAncho(self,ancho):
        self.ancho=ancho    



class Circulos(Figuras):
    def __init__(self,x,y,visible,radio):
        super().__init__(x,y,visible)
        self.radio=radio

    def mostrar(self):
        print(f"El Circulo se encuentra visible: {self.estaVisible()} y se esta localizado en coordenada X,Y {self.getX(),self.getY()}, ademas tiene un radio de: {self.getRadio()} ")     

    def ocultar(self):
        print(f"El Circulo se esta ocultando")    
        
    #Resto de los metodos set y get 
    def getRadio(self):
        return self.radio     
    
    def setRadio(self,radio):
        self.radio=radio

#Instancias los objetos correspondientes
#1.- Crear un primer objeto de la clase Rectangulos que se llame: "rectangulo1", en el cual se introduzca la siguiente información: x=3,y=4, visible=True, ancho y alto 10 y 20 respectivamente. 

rectangulo1=Rectangulos(3,4,True,10,20)

#2.- Mostrar los valores del objeto rectangulo1

rectangulo1.mostrar()

# #3.- Crear otro objeto de la clase Circulos que se llame: "circulos1", en el cual se introduzca la siguiente información: x=3,y=3, visible=True y radio de 6. 

circulo1=Circulos(3,3,True,6)

# #4.- Mostrar los valores del objeto rectangulo1
circulo1.mostrar()

