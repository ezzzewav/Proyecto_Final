from clase_persona import Persona

class Candidato(Persona):
    def __init__(self, nombre, partido, letra):
        super().__init__(nombre, None, None, None, None)
        self.partido = partido
        self.letra = letra
        self.votos = 0

    def __str__(self):
        return f"Nombre: {self.nombre}, Partido: {self.partido}, Letra: {self.letra}, Votos: {self.votos}"