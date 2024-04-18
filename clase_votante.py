from clase_persona import Persona

class Votante(Persona):
    def __init__(self, nombre, edad, cedula, nacionalidad):
        super().__init__(nombre, edad, cedula, nacionalidad, None)
        self.puede_votar = False
        self.voto = None

    def verificar_edad_nacionalidad(self):
        if self.edad >= 18 and self.nacionalidad == "costarricense":
            self.puede_votar = True
        else:
            self.puede_votar = False