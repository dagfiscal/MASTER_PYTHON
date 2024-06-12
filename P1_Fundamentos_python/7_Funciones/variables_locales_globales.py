"""
  VARIABLES LOCALES.-  se definen dentro de la función y no se 
  pueden usar fuera de ellla a no ser que se realice mediante un return

  VARIABLES GLOBALES.- son las que declaran fuera de una función 
  y estan dispobibles fuera y dentro de ella


"""

#Variable Global

numero=23


def mostrarNumero1():
     #Variable local dentro de la funcion 
    numero=34
    #imprime el contenido de la variable local
    print(f"El valor de la variable 'numero' es: {numero}")

def mostrarNumero2():
     
    #imprime el contenido de la variable global
    print(f"El valor de la variable 'numero' es: {numero}")    

def mostrarNumero3():
     
    #Dentro de una variable crear una variable global para utilizar fuera de funcion 
    global num
    num=int(input("Ingresa el valor de num: "))
       

mostrarNumero1()
mostrarNumero2()
mostrarNumero3()
print(f"El valor de la variable 'numero' es: {num}")