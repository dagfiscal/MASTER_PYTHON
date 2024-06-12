def solicitarDatos():
  print("\n")
  #global n1,n2
  n1=float(input("Numero 1: "))
  n2=float(input("Numero 2: "))
  return n1,n2
  

def getCalculadora(n1,n2,opc):
  if opc=="1" or opc=="SUMA":
    resultado=f"{n1} + {n2} = {n1+n2}"
  elif opc=="2" or opc=="RESTA":
    resultado=f"{n1} - {n2} = {n1-n2}" 
  elif opc=="3" or opc=="MULTIPLICACION":
    resultado=f"{n1} * {n2} = {n1*n2}"  
  elif opc=="4" or opc=="DIVISION":
    resultado=f"{n1} / {n2} = {n1/n2}" 
  return resultado    


def esperaTecla():
   # Muestra un mensaje
   print("Presiona cualquier tecla para continuar...")

   # Espera a que el usuario presione una tecla
   input()

