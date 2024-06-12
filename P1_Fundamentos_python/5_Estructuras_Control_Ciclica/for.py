#Ciclo For  Estruxtura iterativa que se ejecuta X veces

# Sintaxis
#  for variable in elemento_iterable (lista, rango, etc)
#     bloque de instrucciones

# Ejemplo 1 Crear un programa que imprima en pantalla 5 veces el @

contador=1

for contador in range(1,6):
    print("@")

# Ejemplo 2 Crear un programa que imprima en los numeros del 1 al 5 y los sume y al final imprima 
# la suma

contador=1
suma=0

for contador in range(1,6):
    print("El numero es: "+str(contador))
    suma+=contador
    #suma=suma+contador

print("El resultado de la suma es: "+str(suma))


# Ejemplo 2 Crear un programa que imprima la tabla de multiplicar

print("... Tabla de Multiplicar ....")
numero=int(input("Ingresa el numero de la tabla de multiplicar: "))

for i in range(1,11):
    multi=numero*i
    print(f"{numero} X {i} = {multi}")
   # print(str(numero)+" X "+str(i)+" = "+str(multi))
   




