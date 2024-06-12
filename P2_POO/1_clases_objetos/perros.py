#Crear una clase y al menos 2 instancias de una clase perros con los atributos: nombre, raza y altura y sus metodos: comer, dormir y ladrar

import os

os.system("clear")

class Perros:

    def __init__(self,nombre,raza,altura):
     self.nombre=nombre
     self.raza=raza
     self.altura=altura

    def setPerro(self):
      return f"El perro se llama: {self.nombre} y es de la raza: {self.raza} y tiene un tamaño de: {self.altura}"

    def comer(self):
      return f"Croquetas 1 vez al día"

    def dormir(self):
      return "Duermen en circulo"

    def ladrar(self):
       return "Wau Wau Wau ..."  
        

#Instaciar objetos 

perro1=Perros("Pequeño","Chihuahua",20)

print(perro1.nombre)
print(perro1.setPerro())
print(perro1.comer())

print(f"Los perros comen {perro1.comer()}")
print(f"Los perros {perro1.dormir()}")
print(f"Los perros ladran haciendo: {perro1.ladrar()}")
