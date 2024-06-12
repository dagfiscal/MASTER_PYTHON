#Estructura de control if

#Ejemplo 1

color="2"

#if simple 
if color=="rojo":
   print("Soy el color Rojo ok ...")

#if compuesto 
if color=="rojo":
   print("Soy el color Rojo ok ...")
else:
   print("Soy otro color ok ...") 


#if anidado 
if color=="rojo":
   print("Soy el color Rojo ok ...")
   if color!="rojo":
     print("Soy otro color ok ...") 


#Ejemplo 2 Adivina mi color?

# color =input("¿Adivina mi color?")
# color=color.upper();

# print ("El color es: ",color)

# if color=="AMARILLO":
#    print("Adivinaste soy el color amarillo ...")
# else:
#    print("Vuelve a intentarlo ... ...")

#Ejemplo 3 Solicitar la edad de una persona e imprimir si eres mayor de edad o no 

 #Convertir el valor a numero por que lo que se re
 #recibe por input es str (string)
 
# year=int(input("¿Edad: ?")) 

# if (year>=18):
#    print("Eres mayor de edad")
# else:
#    print("Eres menor de edad")


#Ejemplo 4 Crear un programa que implemente if anidados

# edad=int(input("Ingresa la edad"))

# if edad>=18:
#    print("Soy mayor de edad")
#    if edad>=65:
#       print("Soy un adulto mayor")
# else:
#    print("Soy menor de edad")      


#Ejemplo 4 Crear un programa que implemente elif 

dia=int(input("Ingresa un dia de la semana: "))

if dia==1:
   print("Soy Domingo")
elif dia==2:
   print("Soy Lunes")
elif dia==3:
   print("Soy Martes")
elif dia==4:
   print("Soy Miercoles")
elif dia==5:
   print("Soy Jueves")
elif dia==6:
   print("Soy Viernes")    
elif dia==7:
   print("Soy Sabado")
else:
   print("No correspondo o ningun dia de la semana")   

