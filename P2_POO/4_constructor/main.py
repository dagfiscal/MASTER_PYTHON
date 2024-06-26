#Programa principal desde la que se manda llamar los objetos de la clase de coches

from coches import Coches

coche1=Coches("Blanco","VW","2024",220,150,5)
coche2=Coches("Azul","Nissan","2020",180,150,6)
coche3=Coches("Negro","Jeep","2010",240,150,4)
coche4=Coches("Amarillo","Renault","2019",180,150,6)

print(coche1.getInfo())
print(coche2.getInfo())
print(coche3.getInfo())
print(coche4.getInfo())


