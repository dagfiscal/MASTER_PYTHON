#Crear un programa que solicite una tabla de multiplicar y con una funcion permita generar e imprimir en pantalla la tabla de multiplicar. El programa debera de preguntar si desea obtener otra tabla de multiplicar con las opciones de SI/NO. Al final que el programa indique que ya se termino ...Gracias ...

#Funcio para crear la tabla de multiplicar
def tablas(numero):
   print(f"Tabla de Multiplicar del {numero}")
   for i in range(1,11):
    print(f"{numero} X {i} = {numero*i}")


#Programa Principal

opcion="SI"
while opcion=="SI":
    tabla=int(input("Ingresa el numero de la tabla de multiplicar: "))
    tablas(tabla)
    opcion=input("¿Deseas otra tabla de multiplicar (SI/NO)?: ")
    opcion=opcion.upper()
    while opcion!="SI" and opcion!="NO":
         opcion=input("¿Deseas otra tabla de multiplicar (SI/NO)?: ")
         opcion=opcion.upper()

if opcion=="NO":
 print("Listo ya termine ... Gracias ...")         



