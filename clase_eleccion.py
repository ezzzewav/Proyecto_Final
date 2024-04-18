import csv

class Eleccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.candidatos = []
        self.votantes = []

    def agregar_candidato(self, candidato):
        self.candidatos.append(candidato)

    def agregar_votante(self, votante):
        self.votantes.append(votante)

    def mostrar_candidatos(self):
        for i, candidato in enumerate(self.candidatos, start=1):
            print(f"{i}. {candidato}")

    def votar(self, votante, candidato):
        if votante.puede_votar:
            candidato.votos += 1
            votante.voto = candidato
            print("Su voto ha sido registrado.")
        else:
            print(f"{votante.nombre} no puede votar por no cumplir con los requisitos.")

    def guardar_votos(self, archivo):
        try:
            with open(archivo, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Nombre', 'Edad', 'Cédula', 'Nacionalidad', 'Género', 'Candidato'])
                for votante in self.votantes:
                    if votante.voto:
                        writer.writerow([votante.nombre, votante.edad, votante.cedula, votante.nacionalidad, votante.genero, votante.voto.nombre])
        except IOError:
            print("Error al guardar los votos.")