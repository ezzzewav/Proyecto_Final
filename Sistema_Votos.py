from clase_persona import Persona
from clase_candidato import Candidato
from clase_votante import Votante
from clase_eleccion import Eleccion

import csv

eleccion = Eleccion("Elecciones 2024")

candidato1 = Candidato("Laura Chinchilla", "Partido PLN", "A")
candidato2 = Candidato("Carlos Alvarado", "Partido PAC", "B")
candidato3 = Candidato("Rodrigo Chaves", "Partido PSD", "C")

eleccion.agregar_candidato(candidato1)
eleccion.agregar_candidato(candidato2)
eleccion.agregar_candidato(candidato3)

exit_system = False
votante = None

while not exit_system:
    print("Bienvenido al Sistema Costarricense de Votaciones.")
    print("Seleccione una opción:")
    print("1) Validar identidad")
    print("2) Votar")
    print("3) Ver cantidad de votos (solo para administradores)")
    print("4) Salir del sistema")

    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))

        if edad < 18:
            print("No puede votar por ser menor de edad.")
            exit_system = True
            continue

        cedula = input("Ingrese su cédula: ")
        nacionalidad = input("Ingrese su nacionalidad: ")
        if nacionalidad != "costarricense":
            print("Lo siento, solo se permite el acceso a personas costarricenses.")
            exit_system = True
            continue

        genero = input("Ingrese su género: ")

        votante = Votante(nombre, edad, cedula, nacionalidad)
        votante.verificar_edad_nacionalidad()
        votante.genero = genero

        if votante.puede_votar:
            eleccion.agregar_votante(votante)
            print("Su identidad ha sido validada. Puede proceder a votar.")
        else:
            print("No cumple con los requisitos para votar.")

    elif opcion == "2":
        if votante:
            if votante.puede_votar:
                print("Seleccione el número correspondiente al candidato:")
                eleccion.mostrar_candidatos()
                letra_candidato = input("Ingrese la letra del candidato al que desea votar: ")

                candidato_seleccionado = None
                for candidato in eleccion.candidatos:
                    if candidato.letra.lower() == letra_candidato.lower():
                        candidato_seleccionado = candidato
                        break

                if candidato_seleccionado:
                    eleccion.votar(votante, candidato_seleccionado)
                    eleccion.guardar_candidatos("candidatos.txt")
                    eleccion.guardar_votos("votos.csv")
                else:
                    print("La letra del candidato seleccionado no es válida.")
            else:
                print("No puede votar por no cumplir con los requisitos.")
        else:
            print("Primero debe validar su identidad.")

    elif opcion == "3":
        password = input("Ingrese la contraseña de administrador: ")
        if password == "1234":
            for candidato in eleccion.candidatos:
                print(f"{candidato.nombre}: {candidato.votos} votos")
        else:
            print("Contraseña incorrecta. Acceso denegado.")

    elif opcion == "4":
        exit_system = True

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

print("Gracias por utilizar el Sistema Costarricense de Votaciones. ¡Hasta pronto!")