from game import *
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)

#Definido o titulo da janela
pygame.display.set_caption("MathKids")

FPS = 500

#Definindo cor da tela
white = (255, 255, 255)

game = game(screen, FPS)

while True:
	# Quando clicar no x para fechar a tela
	for eventos in pygame.event.get():
	    if eventos.type == pygame.QUIT:
	        exit()
	
	game.renderGame(screen, white)

	pygame.display.update()