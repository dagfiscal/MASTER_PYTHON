#Funciones más comunes en las listas


paises=["México","Brasil","España","Canada"]
numeros=[23,12,100,34]

#ordenar ascendentemente

print(numeros)
numeros.sort()
print(numeros)

#Anadir elementos

print(paises)
paises.append("Honduras")
print(paises)

paises.insert(1,"Japón")
print(paises)

#Eliminar elementos

numeros.pop(0)
print(numeros)

numeros.remove(100)
print(numeros)

#Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

#Buscar dentro de una lista 

print("Brasil" in paises)  

#Cuantas veces aparece un valor dentro de una lista
numeros.append(23)
print(numeros)
print(numeros.count(23))

#identificar un indice de un elemento de la lista

print(paises.index("México"))

#Unir listas

print(paises)
paises.extend(numeros)
print(paises)