"""  
 Programación Orinetada a Objetos POO o OOP
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    color="rojo"
    marca="Ferrari"
    modelo="2010"
    velocidad=300
    caballaje=500
    plazas=2

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1

    def getVelocidad(self):
       return self.velocidad

#Fin definir clase

#Crear un objetos o instanciar la clase

coche1=Coches()

print(f"Marca: {coche1.marca} \n Modelo: {coche1.modelo} y su velocidad es: {coche1.velocidad}")

for i in range(1,11):
    coche1.acelerar()

print(f"El coche de la Marca: {coche1.marca} despues de 10 segundos aumentos su velocidad a: {coche1.velocidad}")    



