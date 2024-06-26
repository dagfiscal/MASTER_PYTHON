#Clase 
class Personas:
    def __init__(self, nombre, edad,tel):
        self.nombre = nombre
        self.edad = edad
        self.tel=tel
    
    def info_persona(self):
        print(f"\nHola, mi nombre es {self.nombre}, tengo {self.edad} años. Mi numero de telefono es {self.tel}")

#Herencia La clase Estudiante hereda de la clase Persona
class Estudiantes(Personas):
    def __init__(self, nombre, edad, tel,carrera,matricula):
        super().__init__(nombre,edad,tel)
        self.carrera = carrera
        self.matricula=matricula
    
    def informar_carrera(self):
        print(f"\nSoy alumno {self.nombre} con matricula {self.matricula} y estudio la carrera de {self.carrera}.")

class Docentes(Personas):
    def __init__(self, nombre, edad,tel, modalidad,num_empleado):
        super().__init__(nombre, edad,tel)
        self.modalidad = modalidad
        self.num_empleado=num_empleado
    
    def informar_modalidad(self):
        print(f"\nSoy el docente {self.nombre}, con numero de empleado {self.num_empleado} y trabajo en la carrera de {self.modalidad}.")

#Instaciar objetos de la clase principal

persona1 = Personas("Juan Correa Simental", 25,6181234567)
persona2 = Personas("María Serrano Mata", 22, 6182331456)

persona1.info_persona()
persona2.info_persona()

# #Instaciar objetos de la clase secundaria 
estudiante1 = Estudiantes("Ana Torres Guzman", 20,6181234567, "MECA",2335678)
estudiante1.informar_carrera()
estudiante1.info_persona()
 

docente1 = Docentes("Daniel Fuentes Loera", 40,6183335678, "CLASICA",123)
docente1.informar_modalidad()
docente1.info_persona()



