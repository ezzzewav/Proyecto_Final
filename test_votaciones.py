import unittest
import csv
from io import StringIO
from unittest.mock import patch
import os

from clase_persona import Persona
from clase_candidato import Candidato
from clase_votante import Votante
from clase_eleccion import Eleccion

class TestVotaciones(unittest.TestCase):
    def setUp(self):
        self.eleccion = Eleccion("Elecciones 2024")

        self.candidato1 = Candidato("Laura Chinchilla", "Partido PLN", "A")
        self.candidato2 = Candidato("Carlos Alvarado", "Partido PAC", "B")
        self.candidato3 = Candidato("Rodrigo Chaves", "Partido PSD", "C")

        self.eleccion.agregar_candidato(self.candidato1)
        self.eleccion.agregar_candidato(self.candidato2)
        self.eleccion.agregar_candidato(self.candidato3)
        
    def test_verificar_edad_nacionalidad(self):
        votante = Votante("Kattia", 20, "123456789", "costarricense")
        votante.verificar_edad_nacionalidad()
        self.assertTrue(votante.puede_votar)

        votante = Votante("Daniel", 17, "987654321", "costarricense")
        votante.verificar_edad_nacionalidad()
        self.assertFalse(votante.puede_votar)

        votante = Votante("Sofia", 18, "987654321", "panameña")
        votante.verificar_edad_nacionalidad()
        self.assertFalse(votante.puede_votar)
        
    def test_votar(self):
        votante = Votante("Kattia", 20, "123456789", "costarricense")
        votante.verificar_edad_nacionalidad()

        candidato = Candidato("Laura Chinchilla", "Partido PLN", "A")
        self.eleccion.votar(votante, candidato)

        self.assertEqual(candidato.votos, 1)
        self.assertEqual(votante.voto, candidato)
        
    def test_guardar_candidatos(self):
        self.eleccion.guardar_candidatos("candidatos.txt")  

        with open("candidatos.txt", mode="r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(rows[0], ['Nombre', 'Partido', 'Letra', 'Votos'])
            self.assertEqual(rows[1], ['Laura Chinchilla', 'Partido PLN', 'A', '0'])
            self.assertEqual(rows[2], ['Carlos Alvarado', 'Partido PAC', 'B', '0'])
            self.assertEqual(rows[3], ['Rodrigo Chaves', 'Partido PSD', 'C', '0'])

    def test_guardar_votos(self):
        votante = Votante("Kattia", 20, "123456789", "costarricense")
        votante.verificar_edad_nacionalidad()
        candidato = Candidato("Laura Chinchilla", "Partido PLN", "A")
        self.eleccion.votar(votante, candidato)

        self.eleccion.guardar_votos("votos.csv")

        with open("votos.csv", mode="r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertTrue(rows[0], ['Nombre', 'Edad', 'Cédula', 'Nacionalidad', 'Género', 'Candidato'])
            self.assertTrue(rows[-1], ['Kattia', 20, '123456789', 'costarricense', 'M', 'Laura Chinchilla'])

    def tearDown(self):
        try:
            os.remove("candidatos.txt")
        except FileNotFoundError:
            pass

        try:
            os.remove("votos.csv")
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()
