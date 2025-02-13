class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} y soy {self.profesion}")
        
p = Persona("Ana", 28, "Ingeniera")
print(p)
print (p.presentarse())