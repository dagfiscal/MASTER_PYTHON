# Ciclo While Estruxtura control que itera o repite la ejecución de una serie de 
# instrucciones tantas veces como sea necesario hasta que deje de cumplir la condicion 
#  

# Sintaxis
#  while condicion :
#     bloque de instrucciones
#     actualizacion de contador


# Ejemplo 1 Crear un programa que imprima en pantalla 5 veces el @

i=1
while i<=5:
    print("@")
    i+=1

print("\n")
# Ejemplo 2 Crear un programa que imprima en los numeros del 1 al 5 y los sume y al final imprima 
# la suma

i=1
suma=0
while i<=5:
    print(f"{i}")
    suma+=i
    i+=1

print("El resultado de la suma es: "+str(suma))

print("\n")    


# Ejemplo 2 Crear un programa que imprima la tabla de multiplicar

print("... Tabla de Multiplicar ....")
numero=int(input("Ingresa el numero de la tabla de multiplicar: "))

i=12

while i<=10:
    multi=numero*i
    print(f"{numero} X {i} = {multi}")
    i+=1