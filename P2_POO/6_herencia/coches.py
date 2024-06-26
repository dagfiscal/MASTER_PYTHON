#Clase Principal 
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

#Fin clase padre

#Clases Secundarias
#Se implementa la herencia para compartir los atributos y metodos 

class Camiones(Coches):
  def __init__(self,color,marca,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
    super().__init__(color,marca,modelo,velocidad,caballaje,plazas)
    self.eje=eje
    self.capacidadCarga=capacidadCarga

  def cargar(self,tipo_carga):
      self.tipo_carga=tipo_carga
      return self.tipo_carga

  def setEje(self,eje):
     self.eje=eje

  def getEje(self):
    return self.eje

  def setCapacidadCarga(self,traccion):
     self.capacidadCarga=capacidadCarga

  def getCapacidadCarga(self):
    return self.capacidadCarga

class Camionetas(Coches):
  def __init__(self,color,marca,modelo,velocidad,caballaje,plazas,trasera,cerrada):
    super().__init__(color,marca,modelo,velocidad,caballaje,plazas)
    self.traccion=trasera
    self.cerrada=cerrada

  def transportar(self,num_pasajeros):
      self.num_pasajeros=num_pasajeros
      return self.num_pasajeros

  def setTraccion(self,traccion):
     self.traccion=traccion

  def getTraccion(self):
    return self.traccion

  def setCerrada(self,traccion):
     self.cerrada=cerrada

  def getCerrada(self):
    return self.cerrada