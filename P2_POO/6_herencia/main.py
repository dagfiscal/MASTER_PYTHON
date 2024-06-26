"""   
  Herencia.-  la herencia es el hecho de que una clase puede permitir el uso o implementacion o compartir de los atributos y metodos. Es decir cuando una clase hereda a otra se dice que es una super clase, clase padre o principal que es la que hereda los atributos y metodos a la o las clases llamadas sub clases o clases hijas o secundaias
""" 

from coches import Coches,Camiones,Camionetas

#Crear y muestra dos objetos de la clase padre
coche1=Coches("Blanco","VW","2024",220,150,5)
coche2=Coches("Azul","Nissan","2020",180,150,6)

print(coche1.getInfo())
print(coche2.getInfo())

#Crear y muestra dos objetos de la clase camioneta y camion

camioneta1=Camionetas("Amarilla","Renault","2025",240,250,8,"delantera",True)
print(f"Datos de la Camioneta \n Camioneta: {camioneta1.getMarca()}, traccion: {camioneta1.getTraccion()}")

camion1=Camiones("Negro","Dina","2020",180,300,12,8,2500)
print(f"Datos del Camion \n Camion: {camion1.getMarca()}, la capacidad de carga: {camion1.getCapacidadCarga()}")
