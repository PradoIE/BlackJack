#! /usr/bin/python3
import pygame
import time
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


class Carta:
    def __init__(self, nombre, palo):
        self.image = pygame.image.load('imagenes/{}_{}_small.png'.
                                       format(nombre, palo)).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()


# Se crean la pantalla y el reloj
screen = pygame.display.set_mode([800, 800])
clock = pygame.time.Clock()


# Se llama la imagen de fondo
background = pygame.image.load('imagenes/fondo.jpg').convert()
carta1 = Carta('corazon', 'clean')
carta1.rect.x = 50
carta1.rect.y = 600

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
        screen.blit(carta1.image, [50, 500])
        boton_finalizar.show()
        pygame.display.flip()
        clock.tick(60)

    if menu_prin_done and punt_done and partida_done:
        break
pygame.quit()
