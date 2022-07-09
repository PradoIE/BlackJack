#! /usr/bin/python3
# Se importan los módulos necesarios

import random

# Se crean las variables globales

palos = ('Diamantes', 'Tréboles', 'Espadas', 'Corazones')
nombres = ('Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve',
           'Diez', 'Jota', 'Quina', 'Rey', 'As')
valores = {'Dos': 2, 'Tres': 3, 'Cuatro': 4, 'Cinco': 5, 'Seis': 6, 'Siete': 7,
           'Ocho': 8, 'Nueve': 9, 'Diez': 10, 'Jota': 10, 'Quina': 10,
           'Rey': 10, 'As': 11}
jugando = True

# Se definen las clases a utilizar para el juego: Carta, Mazo, y Fichas


class Carta():
    def __init__(self, palo, nombre):
        self.palo = palo
        self.nombre = nombre
        self.valor = valores[nombre]

    def __str__(self):
        return self.nombre + ' de ' + self.palo


class Mazo():
    def __init__(self):
        self.mazo_completo = []
        for palo in palos:
            for nombre in nombres:
                self.mazo_completo.append(Carta(palo, nombre))

    def barajar(self):
        random.shuffle(self.mazo_completo)

    def repartir(self):
        return self.mazo_completo.pop()

    def __str__(self):
        cartas_del_mazo = ''
        for carta in self.mazo_completo:
            cartas_del_mazo = cartas_del_mazo + carta.__str__() + '\n'
        return cartas_del_mazo


class Mano():
    def __init__(self):
        self.cartas = []
        self.valor = 0
        self.ases = 0

    def sumar_carta(self):
        self.valor = 0
        for carta in self.cartas:
            self.valor += carta.valor

    def cambio_as(self):
        for carta in self.cartas:
            if carta.nombre == 'As':
                self.ases += 1
            else:
                pass
        while self.valor > 21 and self.ases > 0:
            self.valor = self.valor - 10
            self.ases = self.ases - 1

    def __str__(self):
        cartas_mano = ''
        for carta in self.cartas:
            cartas_mano = cartas_mano + carta.__str__() + '\n'
        return cartas_mano


class Fichas:
    def __init__(self):
        self.total = 500
        self.apuesta = 0

    def gana_apuesta(self):
        self.total += self.apuesta

    def pierde_apuesta(self):
        self.total -= self.apuesta

# Funciones de funcionamiento general del juego ----------------------------


# Pide la apuesta al jugador
def apostar(fichas):
    while True:
        try:
            fichas.apuesta = int(input("Coloque su apuesta: "))
        except Exception:
            print("Ese no es un número valido")
        else:
            if fichas.apuesta > fichas.total:
                print('La apuesta no puede superar el número de fichas'
                      ' disponibles: {}'.format(fichas.total))
            else:
                break


# Se come una carta, calcula el valor de la mano y verifica el cambio del AS
def comer(mazo, mano):
    mano.cartas.append(mazo.repartir())
    mano.sumar_carta()
    mano.cambio_as()


# Pregunta si quiere comer
def comer_o_quedarse(mazo, mano):
    global jugando
    while True:
        seleccion = input('Digite "c" para comer o "q" para quedarse: ')
        if seleccion == "c":
            comer(mazo, mano)
        elif seleccion == 'q':
            jugando = False
            break
        else:
            print('Debe escribir "c" o "q"')
            continue
        break


# Enseña las cartas
def ensena_parcial(jugador, dealer):
    print('\n Mano del Dealer: \n')
    print('Carta oculta')
    print(dealer.cartas[1])
    print('\n Mano del jugador: \n')
    print(jugador)
    print('El valor de la mano del jugador es: {}'.format(jugador.valor))


def ensena_completo(jugador, dealer):
    print('\n Mano del Dealer: \n')
    print(dealer)
    print('El valor de la mano del dealer es: {}'.format(dealer.valor))
    print('\n Mano del jugador: \n')
    print(jugador)
    print('El valor de la mano del jugador es: {}'.format(jugador.valor))


# Verificación ganador/perdedor
def jugador_sobrepasa(fichas):
    print("¡El jugador se sobrepasó!")
    fichas.pierde_apuesta()
    print('Fichas del jugador: {}'.format(fichas.total))


def jugador_gana(fichas):
    print("¡El jugador ganó!")
    fichas.gana_apuesta()
    print('Fichas del jugador: {}'.format(fichas.total))


def dealer_sobrepasa(fichas):
    print("¡El dealer se sobrepasó!")
    fichas.gana_apuesta()
    print('Fichas del jugador: {}'.format(fichas.total))


def dealer_gana(fichas):
    print("¡El dealer ganó!")
    fichas.pierde_apuesta()
    print('Fichas del jugador: {}'.format(fichas.total))


# Funcionamiento del juego ---------------------------------------------------
# Se inicializan las fichas del jugador
fichas = Fichas()

while True:
    print('\n\n¡Bienvenido a Blackjack!\nEl objetivo del juego es acercarse '
          'lo más posible a 21 sin sobrepasarse. El dealer come hasta llegar '
          ' a 17. \n')
    # Se crea y baraja el mazo
    mazo = Mazo()
    mazo.barajar()
    # Se crean los jugadores y se reparten dos cartas a cada uno
    jugador = Mano()
    comer(mazo, jugador)
    comer(mazo, jugador)

    dealer = Mano()
    comer(mazo, dealer)
    comer(mazo, dealer)

    # Apuesta

    apostar(fichas)

    # Muestra cartas iniciales

    ensena_parcial(jugador, dealer)

    # Turnos

    while jugando:
        comer_o_quedarse(mazo, jugador)
        ensena_parcial(jugador, dealer)

        if jugador.valor > 21:
            jugador_sobrepasa(fichas)
            break

    if jugador.valor <= 21:

        while dealer.valor < 17:
            comer(mazo, dealer)

        ensena_completo(jugador, dealer)

        if dealer.valor > 21:
            dealer_sobrepasa(fichas)

        elif dealer.valor > jugador.valor:
            dealer_gana(fichas)

        elif dealer.valor < jugador.valor:
            jugador_gana(fichas)

        else:
            print('¡Empate!')

    if fichas.total == 0:
        print("No hay más fichas disponible. Gracias por jugar")
        break

    nueva_mano = input('¿Quiere jugar una nueva mano? Indique "si" o "no": ')

    if nueva_mano == 'si':
        jugando = True
        continue
    elif nueva_mano == 'no':
        print('Gracias por jugar')
        break
