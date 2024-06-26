from clases import *

def borrarPantalla():
  import os  
  os.system("clear")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def menuPrincipal():
  borrarPantalla()
  print("\n\t..::: Sistema de Gestión del Parque Vehicular :::... \n ..::: Menú Principal :::.  \n 1.- Coches  \n 2.- Camiones \n 3.- Camionetas \n 4.- SALIR ")  

def menuSecundario(clase):
  global clases
  clases=clase
  borrarPantalla()
  print("\n\t..::: Sub-Menú :::... \n 1.- Insertar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Regresar ")
  opcion_insertar=input("\t Elige una opción: ").upper()
  if opcion_insertar!="7":
   if opcion_insertar=="1":
     insertar(clases) 
   elif opcion_insertar=="2":
     eliminar(clases)
   elif opcion_insertar=="3":
     actualizar(clases) 
   elif opcion_insertar=="4":
     consultar(clases)
   elif opcion_insertar=="5":
     buscar(clases)
   elif opcion_insertar=="6":
     menuPrincipal()   
  else:
    print("Opción invalida vuelva a intentarlo ... por favor")  
    esperarTecla()  

def insertar(clases):
  borrarPantalla()
  print("\n\t Ingrese los datos del Vehiculo:  ")
  color=input("Color: ")
  marca=input("Marca: ")
  modelo=input("Modelo: ")
  velocidad=input("Velocidad Maxima alcanzada: ")
  caballaje=input("Potencia o Caballaje: ")
  plazas=input("# Plazas: ")
  if clases=="1":
    coche1=Coches(color,marca,velocidad,modelo,caballaje,plazas)
    coche1.getInfo()
  elif clases=="2":
    eje=input("# Ejes: ")
    capacidadCarga=input("Capacidad de carga: ")
    camion1=Camiones(color,marca,velocidad,modelo,caballaje,plazas,eje,capacidadCarga)
    camion1.getInfo()
  elif clases=="3": 
    eje=input("Tracción: ")
    capacidadCarga=input("Cerrada (True/False): ")
    camioneta1=Camionetas(color,marca,velocidad,modelo,caballaje,plazas,traccion,cerrada)
    camioneta1.getInfo() 
  esperarTecla()
  menuSecundario(clases)



def buscar(clases):
  borrarPantalla()
  print("\n\t Actualizar los datos del Vehiculo:  ")
  print("\n Los datos del actuales son: ")
  if clases=="1":
    coche1.getInfo()
  elif clases=="2":
    camion1.getInfo()
  elif clases=="3": 
    camioneta1.getInfo() 
  esperarTecla()
  menuSecundario(clases)