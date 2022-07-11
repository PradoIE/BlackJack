#! /usr/bin/python3
import ast

import pygame
import random
import time

############################################################################
# CLASES Y FUNCIONES DEL JUEGO

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


class Fichas(object):
    def __init__(self, screen):
        self.screen = screen
        self.fichas_total = 500
        self.fichas_apuesta = 0

    def gana_apuesta(self):
        self.fichas_total += self.fichas_apuesta

    def pierde_apuesta(self):
        self.fichas_total -= self.fichas_apuesta

    def apuesta(self):
        self.text1('Fichas disponibles = {}'.format(self.fichas_total),
                   200, 300)
        self.fichas_apuesta = int(self.game_intro())
        return self.fichas_apuesta, self.fichas_total

    def text1(self, word, x, y):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("{}".format(word), True, black)
        self.screen.blit(text, (x, y))
        pygame.display.update()
        return self.screen.blit(text, (x, y))

    def inpt(self):
        word = ""
        self.text1("Coloque su apuesta = ", 200, 350)  # example asking name
        done = True
        while done:
            for event in pygame.event.get():
                self.text1(word, 575, 350)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        word += str(chr(event.key))
                    if event.key == pygame.K_1:
                        word += str(chr(event.key))
                    if event.key == pygame.K_2:
                        word += chr(event.key)
                    if event.key == pygame.K_3:
                        word += chr(event.key)
                    if event.key == pygame.K_4:
                        word += chr(event.key)
                    if event.key == pygame.K_5:
                        word += chr(event.key)
                    if event.key == pygame.K_6:
                        word += chr(event.key)
                    if event.key == pygame.K_7:
                        word += chr(event.key)
                    if event.key == pygame.K_8:
                        word += chr(event.key)
                    if event.key == pygame.K_9:
                        word += chr(event.key)
                    if event.key == pygame.K_RETURN:
                        done = False
        self.text1(word, 575, 350)
        return word

    def game_intro(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        intro = False

            valor_apuesta = self.inpt()
            pygame.display.update()
            return valor_apuesta


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


##############################################################################
#  random
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
gray = (150, 150, 150)


class Boton:
    def __init__(self, text,  pos, font, bg='gray', feedback='Sin feedback'):
        self.x, self.y = pos
        self.font = pygame.font.SysFont('Arial', font)
        self.text = self.font.render(text, 1, pygame.Color('Black'))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.feedback = feedback

    def show(self):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True


class Carta_GUI:
    def __init__(self, nombre, palo):
        self.image = pygame.image.load('imagenes/cartas/{}_{}.png'.
                                       format(nombre, palo)).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()


# Se crean la pantalla y el reloj
screen = pygame.display.set_mode([800, 800])
clock = pygame.time.Clock()


# Se llama la imagen de fondo
background = pygame.image.load('imagenes/fondo.jpg').convert()

# Se inicializan los botones del menu principal y puntuaciones más altas
boton_iniciar = Boton(' Iniciar Juego ', (247, 100), font=50,
                      bg=gray, feedback='Iniciar juego clickeado')
boton_puntuaciones = Boton(' Puntuaciones más altas', (133.5, 350), font=50,
                           bg=gray, feedback='Puntuaciones más altas clikeado')
boton_salir = Boton(' Salir de juego ', (236.5, 600), font=50,
                    bg=gray, feedback='Salir del juego clickeado')
boton_regresar = Boton(' Regresar al menu principal ', (93.5, 749), font=50,
                       bg=gray, feedback='Regresar al menu principal clikeado')
boton_finalizar = Boton(' Finalizar partida ', (574, 769), font=30,
                        bg=gray, feedback='Finalizar partida clikeado')
boton_comer = Boton(' Comer ', (23, 769), font=30,
                    bg=gray, feedback='Comer clikeado')
boton_quedarse = Boton(' Quedarse ', (150, 769), font=30,
                       bg=gray, feedback='Quedarse clikeado')
boton_nueva_mano = Boton(' Nueva mano ', (350, 769), font=30,
                         bg=gray, feedback='Nueva mano clikeado')


menu_prin_done = False
punt_done = False
partida_done = False
lista = []
while True:
    # Bucle Menu principal
    while not menu_prin_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_prin_done = True
                punt_done = True
                partida_done = True
            if boton_iniciar.click(event):
                print(boton_iniciar.feedback)
                screen.blit(background, [0, 0])
                fichas = Fichas(screen)
                partida_done = False
                menu_prin_done = True
                punt_done = True

            if boton_puntuaciones.click(event):
                print(boton_puntuaciones.feedback)
                menu_prin_done = True
                punt_done = False
                partida_done = True

            if boton_salir.click(event):
                print(boton_salir.feedback)
                menu_prin_done = True
                punt_done = True
                partida_done = True

        screen.blit(background, [0, 0])
        boton_iniciar.show()
        boton_puntuaciones.show()
        boton_salir.show()
        pygame.display.flip()

        clock.tick(60)
    # Bucle Puntuaciones
    while not punt_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_prin_done = True
                punt_done = True
                partida_done = True
            if boton_regresar.click(event):
                print(boton_regresar.feedback)
                punt_done = True
                menu_prin_done = False
                partida_done = True

        screen.blit(background, [0, 0])
        puntuaciones = open('Puntuaciones.txt', 'r')
        lista_final = []
        lista = ast.literal_eval(puntuaciones.read())
        counter = 0
        for i in lista:
            puntuacion = Boton(str(i), (400, 100 + 50 * counter), font=30, bg=gray)
            lista_final.append(puntuacion)
            counter += 1
        for x in lista_final:
            x.show()
        boton_regresar.show()
        pygame.display.flip()

        clock.tick(60)

    # Bucle partida
    nueva_mano = False
    if not partida_done:
        screen.blit(background, [0, 0])
        z = True
        while z:
            try:
                x, y = fichas.apuesta()
            except Exception:
                print('hola')
            else:
                if x > y:
                    fichas.text1('La apuesta supera el número '
                                 'de fichas', 100, 500)
                    time.sleep(2)
                    screen.blit(background, [0, 0])
                else:
                    break
        z = False
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
    carta_oculta = Carta_GUI('carta', 'vuelta')
    carta_no_oculta = Carta_GUI(dealer.cartas[1].nombre, dealer.cartas[1].palo)
    screen.blit(background, [0, 0])
    screen.blit(carta_oculta.image, [50, 50])
    screen.blit(carta_no_oculta.image,  [200, 50])
    mifuente = pygame.font.SysFont('Arial',50)
    mitexto = mifuente.render('¡Dealer ganó!',0,(255,255,255))
    mifuente2 = pygame.font.SysFont('Arial',50)
    mitexto2 = mifuente2.render('¡Jugador ganó!',0,(255,255,255))
    mifuente3 = pygame.font.SysFont('Arial',50)
    mitexto3 = mifuente3.render('¡Empate!',0,(255,255,255))
    while not partida_done:
        # Muestra cartas iniciales
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_prin_done = True
                punt_done = True
                partida_done = True
                
            if boton_comer.click(event):
                print(boton_comer.feedback)
                comer(mazo, jugador)
                print(jugador.valor)
                print(dealer.valor)
                if jugador.valor > 21:
                    #print ('Delear ganó')
                    screen.blit(mitexto,(200,300))
                    pygame.display.update
                    fichas.pierde_apuesta()
                    
            if boton_quedarse.click(event):
                print(boton_quedarse.feedback)
                print(jugador.valor)
                print(dealer.valor)
                
        
                if jugador.valor > 21 :
                    #print ('Delear ganó')
                    screen.blit(mitexto,(200,300))
                    pygame.display.update
                    fichas.pierde_apuesta()
                if dealer.valor == 21 :
                    #print ('Dealer ganó')
                    screen.blit(mitexto,(200,300))
                    pygame.display.update
                    fichas.pierde_apuesta()
                if dealer.valor > 21 :
                    #print ('jugador ganó')
                    screen.blit(mitexto2,(200,300))
                    pygame.display.update
                    fichas.gana_apuesta()
                if dealer.valor < 21 and dealer.valor > jugador.valor :
                    #print ('Dealer ganó')
                    screen.blit(mitexto,(200,300))
                    pygame.display.update
                    fichas.pierde_apuesta()
                if jugador.valor > dealer.valor and jugador.valor < 21 :
                    #print ('jugador ganó')
                    screen.blit(mitexto2,(200,300))
                    pygame.display.update
                    fichas.gana_apuesta()
                if jugador.valor == dealer.valor:
                    #print ('jugador ganó')
                    screen.blit(mitexto3,(200,300))
                    pygame.display.update
                             
                while dealer.valor < 17:
                    comer(mazo, dealer)
                cartas_dealer = []
                for carta in dealer.cartas:
                    carta_g = Carta_GUI(carta.nombre, carta.palo)
                    cartas_dealer.append(carta_g)

                i = 0
                for carta_g in cartas_dealer:
                    screen.blit(carta_g.image, [50 + 150*i, 50])
                    i += 1
            if boton_finalizar.click(event):
                print(boton_finalizar.feedback)
                lista.append(fichas.fichas_total)
                puntuaciones_anteriores = open('Puntuaciones.txt', 'r')
                puntuaciones_anteriores_lista = ast.literal_eval(puntuaciones_anteriores.read())
                lista_nueva = lista + puntuaciones_anteriores_lista
                puntuaciones_anteriores.close()
                lista_nueva.sort(reverse=True)
                puntuaciones_nuevas = open('Puntuaciones.txt', 'w+')
                puntuaciones_nuevas.write(str(lista_nueva))
                puntuaciones_nuevas.close()
                punt_done = True
                menu_prin_done = False
                partida_done = True

            if boton_nueva_mano.click(event):
                print(boton_nueva_mano.feedback)
                nueva_mano = True

        cartas_jugador = []
        for carta in jugador.cartas:
            carta_g = Carta_GUI(carta.nombre, carta.palo)
            cartas_jugador.append(carta_g)

        i = 0
        for carta_g in cartas_jugador:
            screen.blit(carta_g.image, [50 + 150*i, 500])
            i += 1
        boton_apuesta = Boton(' Apuesta: {} '.format(fichas.fichas_apuesta),
                              (50, 400), font=30, bg=gray)
        boton_disponible = Boton(' Disponible: {} '.format(abs
                                 (fichas.fichas_apuesta-fichas.fichas_total)),
                                 (400, 400), font=30, bg=gray)
        boton_apuesta.show()
        boton_disponible.show()
        boton_finalizar.show()
        boton_comer.show()
        boton_quedarse.show()
        boton_nueva_mano.show()
        pygame.display.flip()
        if nueva_mano:
            break
        clock.tick(60)

    if menu_prin_done and punt_done and partida_done:
        break
pygame.quit()
