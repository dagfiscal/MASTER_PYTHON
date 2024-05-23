"""  

 List (Array)
 son colleciones o conjunto de datos/valores bajo 
 un mismo nombre, para acceder a los valores se
 hace con un indice numerico 

 Nota: sus valores si son modificables


"""

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido

# numeros=[23,45,56,78]

# for i in numeros:
#     print(i)

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 

# palabras=["Hola","mes","2024","saludos"]

# palabra=input("¿Cual es la palabra a buscar? ")

# i=0
# noencontre=True
# while i<len(palabras):
#     if palabras[i]==palabra:
#         noencontre=False
#         print(f"la palabra {palabras[i]} la encontre en la posicion {i} ")
#     i+=1 

# if noencontre:
#     print(f"la palabra {palabra} NO se encuentra en la lista") 


#Añadir elementos a la lista

# numeros=[23,45,56,78]
# for i in numeros:
#     print(i)


# numeros.append(100)
# print("\n")
# for i in numeros:
#     print(i)

peliculas=["Batman"]
print(peliculas)
opcion="SI"
while opcion=="SI":
   pelicula=input("Introduce la pelicula: ")
   peliculas.append(pelicula)
   opcion=input("¿Deseas introducir otra pelicula (SI/NO)? ")
   opcion=opcion.upper()

print(peliculas)

#Quitar una pelicula

peliculas.remove("Batman")
print(peliculas)
peliculas.pop(2)
print(peliculas)



#Recorrer una lista 

# for i in numeros:
#     print(f"{numeros.index(i)}: {i}")

# i=0
# while i<len(numeros):
#     print(f"{i}: {numeros[i]}")
#     i+=1