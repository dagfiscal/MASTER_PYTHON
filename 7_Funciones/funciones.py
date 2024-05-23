
"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
   1.- Funcion que no recibe parametros y no regresa valor
   2.- Funcion que no recibe parametros y regresa valor
   3.- Funcion que recibe parametros y no regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""

#Ejemplo 1 Crear una funcion para imprimir nombres de personas


#Definir funcion  1.- Funcion que no recibe parametros y no regresa valor
# def solicitarNombres():
#     nombre=input("Introduce el nombre de una persona: ")

# #invocar la funcion
# solicitarNombres()


#Parametros en la funcion 3.- Funcion que recibe parametros y no regresa valor
#Ejemplo 2 Crear una funcion que solicite dos numeros para realizar una suma

# def sumaDosNumeros(n1,n2):
#     suma=n1+n2
#     print(f"{n1}+{n2}={suma}")

# sumaDosNumeros(3,4)

# def mostrarNombreUsuario(nombre):
#     print(f"El nombre del usuario es: {nombre}")

# mostrarNombreUsuario("Daniel Guzman Loera")    


#Ejemplo 3 Crear una funcion que utilice parametros 


# def mostrarNombreUsuario(nombre,telefono):
#     print(f"El nombre del usuario es: {nombre} y su # de telefono es: {telefono}")


# nom=input("Nombre del usuario: ")
# tel=input("Telefono: ")

# mostrarNombreUsuario(nom,tel)   

#ejemplo 4 Funcio que recibe NO RECIBE parametros pero si regresa valor

# def suma():
#     n1=int(input("Numero #1: "))
#     n2=int(input("Numero #2: "))
#     suma=n1+n2
#     return suma

# sum=suma()

# print(f"La suma es: {sum}")


#ejemplo 5 Funcio que recibe parametros Y si regresa valor

# def suma(num1,num2):
#     suma=num1+num2
#     return suma


# n1=int(input("Numero #1: "))
# n2=int(input("Numero #2: "))
# sum=suma(n1,n2)

# print(f"La suma es: {sum}")

#Ejemplo 6 Funcion con parametros opcionales

def datosUsuario(nom,tel,email=None):
   print(f"Nombre Completo: {nom}")
   print(f"Telefono: {tel}")

   if email!=None:
     print(f"E-mail: {email}")


datosUsuario("Ernesto",6181234567,"ernesto@gmail.com")
print("\n")
datosUsuario("Gustavo",6181234567)











