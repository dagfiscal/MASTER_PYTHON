""" 
 Crear un programa que sirva como una calculadora básica que Muestre en pantalla un menu 
 de opciones para realizar alguna de las operaciones básicas (+,-,*,/). 

 Requisitos:
 1.- Utilizar una funcione
 2.- Que salga del programa hasta que el usuario ingrese la palabra "SALIR" o la opcion "5"


"""
	
import os

from varias_funciones import *


# def solicitarDatos():
#   print("\n")
#   global n1,n2
#   n1=float(input("Numero 1: "))
#   n2=float(input("Numero 2: "))
  

# def getCalculadora(n1,n2,opc):
#   if opc=="1" or opc=="SUMA":
#     resultado=f"{n1} + {n2} = {n1+n2}"
#   elif opc=="2" or opc=="RESTA":
#     resultado=f"{n1} - {n2} = {n1-n2}" 
#   elif opc=="3" or opc=="MULTIPLICACION":
#     resultado=f"{n1} * {n2} = {n1*n2}"  
#   elif opc=="4" or opc=="DIVISION":
#     resultado=f"{n1} / {n2} = {n1/n2}" 
#   return resultado    


# def esperaTecla():
#    # Muestra un mensaje
#    print("Presiona cualquier tecla para continuar...")

#    # Espera a que el usuario presione una tecla
#    input()

opcion="1"

while opcion!="5" or opcion!="SALIR":
  #Para Unix/Linux/MacOS/BSD
  os.system ("clear") 
  print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- SALIR ")
  opcion=input("\t Elige una opción: ").upper()
 
  if opcion!="5" and opcion!="SALIR":
     n1,n2=solicitarDatos()
     print(getCalculadora(n1,n2,opcion))
     esperaTecla()
  else: 
     print("\n\t :::: Terminar la Ejecución del SW :::")
     break   




