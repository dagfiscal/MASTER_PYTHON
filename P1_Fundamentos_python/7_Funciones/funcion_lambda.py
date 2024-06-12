# Son funciones pequeñas para tareas muy especificas y rapidas en estas funciones
#no es necesario con la palabra "def"

#Ejemplo crear una funcion lambda para calcular el porciento de una cantidad

porcentaje_cantidad=lambda cant,porciento,: cant*(porciento/100)

cantidad=int(input("Cantidad: "))
porcentaje=float(input("Porcentaje: "))

print(f"El {porcentaje} % de {cantidad} es: {porcentaje_cantidad(cantidad,porcentaje)}")