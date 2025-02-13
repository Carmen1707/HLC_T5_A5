class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

class Estudiante(Persona):
    def __init__(self, nombre, edad, dni, centro, curso, matricula):
        super().__init__(nombre, edad, dni)
        self.centro = centro
        self.curso = curso
        self.matricula = matricula

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} y estudio en el {self.centro}")

p = Persona("Ana", 28, "Ingeniera")
print(p)
print (p.presentarse())