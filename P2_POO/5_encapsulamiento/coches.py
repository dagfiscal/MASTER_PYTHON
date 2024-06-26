"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.

METODO CONSTRUCTOR.- Este metodo especial dentro de una clase y se utiliza para dar un valor a los atributos del objeto al crearlo, es el primer metodo que se ejecuta al crear el objeto y se manda llamar automaticamente al crearlo, es decir este metodo puede recibir parametros al momento de crear el objeto 

Cuando se crear un metodo constructor se utiliza la funcion _init_(), para que se llame automáticamente cada vez que se utiliza la clase para crear un nuevo objeto.

El self es un parámetro es una referencia a la instancia actual de la clase y se utiliza para acceder a variables que pertenecen a la clase.

No es necesario que tenga nombre self, puedes llamarlo como quieras, pero tiene que ser el primer parámetro de cualquier función de la clase. Es decir por regla se utiliza en la palabra self pero puede ser llamado con otro nombre por ejemplo: valor, abd, parametro, etc.

"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    
    #Metodo CONSTRUCTOR, los valores de los atributos ya no se asignan de manera 
    #predeterminada si no depende de lo que el usuario introduce desde que se instancia una clase es decir se crea el objeto
    def __init__(self, color,marca,modelo,velocidad,caballaje,plazas):
      self.color=color 
      self.marca=marca
      self.modelo=modelo
      self.velocidad=velocidad
      self.caballaje=caballaje
      self.plazas=plazas
      
    ##Atributos publicos y privados encapsulamiento o visibilidad
    publico_var="Soy una variable publica"
    __privada_var="Soy una variable privada"  
        
    #Para utilizar un atributo privado hay que utilizar un metodo get
    def getPrivadaVar(self):
       return self.__privada_var   
   
    #Metodo privado 
    def __metodoPrivado(self):
       print("Soy un metodo privado")

    def getMetodoPublico(self):
       self.__metodoPrivado()

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1  

    def getColor(self):
      return self.color

    def setColor(self,color):
      self.color=color 

    def getMarca(self):
      return self.marca

    def setMarca(self,marca):
      self.marca=marca 

    def getModelo(self):
      return self.modelo

    def setModelo(self,modelo):
      self.modelo=modelo        

    def getVelocidad(self):
       return self.velocidad

    def setVelocidad(self,velocidad):
      self.velocidad=velocidad 

    def getCaballaje(self):
       return self.caballaje

    def setCaballaje(self,caballaje):
      self.caballaje=caballaje  

    def getPlazas(self):
       return self.plazas

    def setPlazas(self,plazas):
      self.plazas=plazas 


    def getInfo(self):
        return f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp \n"

#Fin definir clase

