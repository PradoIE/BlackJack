#! /usr/bin/python3
import pygame
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
carta1.rect.x = (50)
carta1.rect.y = (600)

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
                menu_prin_done = True
                punt_done = True
                partida_done = False
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
