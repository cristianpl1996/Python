# Modulos
import pygame, sys
from pygame.locals import *

# Constantes.
WIDTH=300
HEIGHT=300

# Clases y Funciones.
def main():
	pygame.init()
	pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
	pygame.display.set_caption("Pygame")
	reloj = pygame.time.Clock()
	while True:	
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
		reloj.tick(20)
		pantalla.fill((255,255,255))
		pygame.display.update()

if __name__ == "__main__":
    main()