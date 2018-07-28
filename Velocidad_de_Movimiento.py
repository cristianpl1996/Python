import pygame, sys
from pygame.locals import *

def main():
	pygame.init()
	pantalla=pygame.display.set_mode((480,300))
	pygame.display.set_caption("Velocidad de Movimiento")
	reloj=pygame.time.Clock()
	imagen=pygame.image.load("imagen.png")
	x,y=100,100
	vx,vy=0,0
	r1=pygame.Rect(250,70,25,500)
	while True:
		pantalla.fill((255,255,255))
		for evento in pygame.event.get():
			if evento.type==QUIT:
				pygame.quit()
				sys.exit()
			if evento.type==KEYDOWN:
				if evento.key==K_LEFT:
					vx-=10
				if evento.key==K_RIGHT:
					vx+=10
				if evento.key==K_UP:
					vy-=10
				if evento.key==K_DOWN:
					vy+=10			
			if evento.type==KEYUP:			
				if evento.key==K_LEFT:
					vx=0
				if evento.key==K_RIGHT:
					vx=0
				if evento.key==K_UP:
					vy=0
				if evento.key==K_DOWN:
					vy=0			
		x+=vx
		y+=vy				
		reloj.tick(20)	
		pantalla.blit(imagen,(x,y))
		pygame.draw.rect(pantalla,(0,0,0),r1)
		pygame.display.update()

main()	