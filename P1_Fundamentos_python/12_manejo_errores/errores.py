
#ejemplo 1 Cuando una variable no se genera
# try:
#     nombre=input("Dame tu nombre: ")

#     if len(nombre)>1:
#         nombre_usuario="El nombre es: "+nombre

#     print(nombre_usuario)    
# except:
#     print("Es necesario que introducir un nombre de usuario")    

#Ejemplo 2 cuando se solicita un numero y se captura una letra 
# try:
#     numero=int(input("Ingresa un numero: "))

#     if numero>0:
#         print("Soy un numero entero positivo")
#     else:
#         print("Soy un numero entero negativo")    
# except:
#     print("Ingresa un numero por favor")        
# else:
#     print("Todo Terminado ...Correcto") #Esto sale si no entra en la excepcion, es decir si no genera un error
# finally:
#     print("Listo Termine")   #Se ejecuta si la excepcion se genera o no       

#ejemplo 3 Crear multiples excepciones
try:
    numero=int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es: "+str(numero*numero))
except TypeError:
    print("Debes de convertir el numero a entero")
except ValueError:
    print("Debes de introducir un numero no se puede convertir un numero a cadena")    

