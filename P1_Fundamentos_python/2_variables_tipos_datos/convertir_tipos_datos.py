#Convertir tipos de datos 

texto="Soy una cadena"
numero=23

#Asi no se puede utilizar por que no se puede concatener Str con int por 
#por lo tanto hay que realizar una conversion de datos 
# print(texto+" y el valor de "+numero)

#Se utiliza una funcion 
numero_str=str(numero)

print(texto+" y el valor de "+numero_str)

numero2=45
numero_int=int(numero_str)

suma=numero2+numero_int

print(str(numero2)+" + "+numero_str+" = "+str(suma))

numero3=33
print(numero3)
print(type(numero3))

numero3=float(numero3)
print(numero3)
print(type(numero3))

numero3=str(numero3)
print(numero3)
print(type(numero3))


