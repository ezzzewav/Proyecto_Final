class Persona:
    def __init__(self, nombre, edad, cedula, nacionalidad, genero):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.nacionalidad = nacionalidad
        self.genero = genero

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Cédula: {self.cedula}, Nacionalidad: {self.nacionalidad}, Género: {self.genero}"