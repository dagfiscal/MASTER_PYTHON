#Programa principal desde la que se manda llamar los objetos de la clase de coches
import os
from coches import Coches

os.system("clear")

coche1=Coches("Blanco","VW","2024",220,150,5)

#Visibilidad o encapculamiento 
print(coche1.publico_var) #imprimir un atributo publico
print(coche1.getMarca())  #utilizar un metodo publico

# Como esto no es posible aun atributo privado se puede acceder a traves de un metodo publico
#print(objeto.__privada_var) 
print(coche1.getPrivadaVar())

#Como no se puede ejecutar un metodo privado solo es posible desde un metodo publico
#coche1.__metodoPrivado()
coche1.getMetodoPublico()







