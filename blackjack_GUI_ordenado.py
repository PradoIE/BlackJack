#! /usr/bin/python3
import pygame
import time
import random
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
gray = (150, 150, 150)


class Play(object):

    def __init__(self, screen):
        self.screen = screen
        self.fichas_total = 500
        self.fichas_apuesta = 0

    def gana_apuesta(self):
        self.fichas_total += self.fichas_apuesta

    def pierde_apuesta(self):
        self.fichas_total -= self.fichas_apuesta

    def apuesta(self):
        self.text1('Fichas disponibles = {}'.format(self.fichas_total), 200, 300)
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




ha = ('ha.png')
h2 = ('h2.png')
h3 = ('h3.png')
h4 =('h4.png')
h5= ('h5.png')
h6 = ('h6.png')
h7 = ('h7.png')
h8 = ('h8.png')
h9 =('h9.png')
h10= ('h10.png')
hj = ('h8.png')
hq =('hj.png')
hk= ('hk.png')

sa = ('sa.png')
s2 = ('s2.png')
s3 = ('s3.png')
s4 =('s4.png')
s5= ('s5.png')
s6 = ('s6.png')
s7 = ('s7.png')
s8 = ('s8.png')
s9 =('s9.png')
s10= ('s10.png')
sj = ('sj.png')
sq =('sq.png')
sk= ('sk.png')

da = ('da.png')
d2 = ('d2.png')
d3 = ('d3.png')
d4 =('d4.png')
d5= ('d5.png')
d6 = ('d6.png')
d7 = ('d7.png')
d8 = ('d8.png')
d9 =('d9.png')
d10= ('d10.png')
dj = ('d8.png')
dq =('dj.png')
dk= ('dk.png')

ca = ('ca.png')
c2 = ('c2.png')
c3 = ('c3.png')
c4 =('c4.png')
c5= ('c5.png')
c6 = ('c6.png')
c7 = ('c7.png')
c8 = ('c8.png')
c9 =('c9.png')
c10= ('c10.png')
cj = ('c8.png')
cq =('cj.png')
ck= ('ck.png')
mazo= [ha,h2,h3,h4,h5,h6,h7,h8,h9,h10,hj,hq,hk,da,d2,d3,d4,d5,d6,d7,d8,d9,d10,dj,dq,dk,ca,c2,c3,c4,c5,c6,c7,c8,c9,c10,cj,cq,ck,sa,s2,s3,s4,s5,s6,s7,s8,s9,s10,sj,sq,sk]

carta1_jugador= random.sample(mazo,1)
Strcarta1_jugador = ''.join(carta1_jugador)

carta1_dealer = random.sample(mazo,1)
Strcarta1_dealer = ''.join(carta1_dealer)

carta2_jugador= random.sample(mazo,1)
Strcarta2_jugador = ''.join(carta2_jugador)

carta2_dealer = random.sample(mazo,1)
Strcarta2_dealer = ''.join(carta2_dealer)

cartaextra = random.sample(mazo,1)
Strcartaextra = ''.join(cartaextra)

class Carta:
    def __init__(self, nombre, palo):
        self.image = pygame.image.load(Strcarta1_jugador.
                                       format(nombre, palo)).convert()
        self.image2 = pygame.image.load(Strcarta2_jugador.
                                       format(nombre, palo)).convert()
        
        self.image3 = pygame.image.load(Strcarta1_dealer.
                                       format(nombre, palo)).convert()
        self.image4 = pygame.image.load(Strcarta2_dealer.
                                       format(nombre, palo)).convert()
        self.imageback = pygame.image.load('back.png'.
                                       format(nombre, palo)).convert()

        self.imagemazo = pygame.image.load('back.png'.
                                       format(nombre, palo)).convert()
        self.imageextra = pygame.image.load(Strcartaextra.
                                       format(nombre, palo)).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

valores = {'ha.png': 1,'h2.png': 2, 'h3.png': 3, 'h4.png': 4, 'h5.png': 5, 'h6.png': 6, 'h7.png': 7, 'h8.png': 8, 'h9.png': 9, 'h10.png': 10, 'hj.png': 10, 'hq.png' :10, 'hk.png': 10, 'ha.png': 11,'sa.png': 1,'s2.png': 2, 's3.png': 3, 's4.png': 4, 's5.png': 5, 's6.png': 6, 's7.png': 7, 's8.png': 8, 's9.png': 9, 's10.png': 10, 'sj.png': 10, 'sq.png': 10, 'sk.png': 10, 'sa.png': 11, 'da.png': 1,'d2.png': 2, 'd3.png': 3, 'd4.png': 4, 'd5.png': 5, 'd6.png': 6, 'd7.png': 7, 'd8.png': 8, 'd9.png': 9, 'd10.png': 10, 'dj.png': 10, 'dq.png' :10, 'dk.png': 10, 'da.png': 11, 'ca.png': 1,'c2.png': 2, 'c3.png': 3, 'c4.png': 4, 'c5.png': 5, 'c6.png': 6, 'c7.png': 7, 'c8.png': 8, 'c9.png': 9, 'c10.png': 10, 'cj.png': 10, 'cq.png': 10, 'ck.png': 10, 'ca.png': 11}

valor1_jugador = (valores[Strcarta1_jugador])
valor2_jugador = (valores[Strcarta2_jugador])

valor1_dealer= (valores[Strcarta1_dealer])
valor2_dealer = (valores[Strcarta2_dealer])

def suma (valor1, valor2):
        return valor1 + valor2

mazo_jugador = suma(valor1_jugador, valor2_jugador)
mazo_dealer = suma(valor1_dealer, valor2_dealer)
print (mazo_dealer)

if mazo_dealer <=16:
    running = True
else:
    running = False

print (running)
    
    

# Se crean la pantalla y el reloj
screen = pygame.display.set_mode([800, 800])
clock = pygame.time.Clock()


# Se llama la imagen de fondo
background = pygame.image.load('fondo.jpg').convert()
carta1j = Carta ('aleatorio', 'aleatorio')
carta1j.rect.x = (50)
carta1j.rect.y = (600)
carta2j = Carta ('alertorio', 'aleatorio')
carta2j.rect.x = (50)
carta2j.rect.y = (600)
carta1d = Carta ('aleatorio', 'aleatorio')
carta1d.rect.x = (50)
carta1d.rect.y = (600)
carta2d = Carta ('aleatorio', 'aleatorio')
carta2d.rect.x = (50)
carta2d.rect.y = (600)
cartaback = Carta ('aleatorio', 'aleatorio')
cartaback.rect.x = (50)
cartaback.rect.y = (600)
cartaextra = Carta ('aleatorio', 'aleatorio')
cartaextra.rect.x = (50)
cartaextra.rect.y = (600)

cartamazo = Carta ('aleatorio', 'aleatorio')
cartamazo.rect.x = (50)
cartamazo.rect.y = (600)
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
print(boton_finalizar.size)

menu_prin_done = False
punt_done = False
partida_done = False
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
                #########################################################################################
                screen.blit(background, [0, 0])
                z = True
                while z:
                    try:
                        x, y = Play(screen).apuesta()
                    except Exception:
                        print('hola')
                    else:
                        if x > y:
                            Play(screen).text1('La apuesta supera el número de fichas', 100, 500)
                            time.sleep(2)
                            break
                        else:
                            partida_done = False
                            menu_prin_done = True
                            punt_done = True
                            break
            z = False

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
        boton_regresar.show()
        pygame.display.flip()

        clock.tick(60)

    # Bucle partida
    while not partida_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_prin_done = True
                punt_done = True
                partida_done = True
            if boton_finalizar.click(event):
                print(boton_finalizar.feedback)
                punt_done = True
                menu_prin_done = False
                partida_done = True


        screen.blit(background, [0, 0])
        screen.blit(carta1j.image, [300, 500])
        screen.blit(carta2j.image2, [400, 500])
        screen.blit(carta1d.image3, [300, 100])
        screen.blit(cartaback.imageback, [300, 100])
        screen.blit(carta2d.image4, [400, 100])
        screen.blit(cartamazo.imagemazo, [700, 300])
        boton_finalizar.show()
        pygame.display.flip()

    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = True
            if boton_finalizar.click(event):
                print(boton_finalizar.feedback)
                punt_done = True
                menu_prin_done = False
                partida_done = True
        #screen.blit(background, [0, 0])
        screen.blit(cartaextra.imageextra, [500, 100])
        boton_finalizar.show()
        pygame.display.flip()
        clock.tick(60)

        clock.tick(60)
    if menu_prin_done and punt_done and partida_done:
        break
pygame.quit()
