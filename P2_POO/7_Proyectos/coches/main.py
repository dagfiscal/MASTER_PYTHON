#Crear un programa que permita Gestionar (Administrar) el parque vehicular de una empresa transportista.
#Notas: 
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2.- Utilizar el paradigma OO  

from funciones import *


opcion=True 

while opcion:
 menuPrincipal()
 opcion=input("\t Elige una opción: ").upper()
 
 if opcion!="4":
  if opcion=="1" or opcion=="2" or opcion=="3":
    menuSecundario(opcion)    
  else:
    print("Opción invalida vuelva a intentarlo ... por favor")  
    esperarTecla()      
 else:  
  opcion=False    
  print("Terminaste la ejecucion del SW") 
 
 
   