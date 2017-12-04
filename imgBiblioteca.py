"""
	Autor: Levy Santiago
	Última modificação: 04/12/2017
"""

from random import randint
from area import *
from campo import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

#Quantidade maxima de imagens para serem geradas
QTD_IMAGENS = 10

#O valor anterior do valor aleatorio gerado para as imagens
valorRandAnterior = randint(1, 	QTD_IMAGENS)

def multiplicarImagem(screen, caminhoImagem, quantidade):
	imagem = pygame.image.load(caminhoImagem)

	linElementos = quantidade // 2
	#Calculando valores iniciais
	inicioX = (SCREEN_WIDTH - (imagem.get_width() * linElementos)) // 2 

	inicioY = 70
	
	x = inicioX
	y = inicioY

	for i in range(0, quantidade):
		screen.blit(imagem,(x,y))
		x += imagem.get_width()
		if(i == linElementos-1):
			y += imagem.get_height()
			x = inicioX
			linElementos += linElementos

def gerarAreas(screen):
	listaAreas = []
	imagem = area("imagens/field.png", 10)
	
	imagem.setX((SCREEN_WIDTH // 2) - imagem.getWidth())
	y = SCREEN_HEIGHT // 2
	imagem.setY(y)

	listaAreas.append(imagem)

	x = SCREEN_WIDTH // 2
	imagem = area("imagens/field.png", 11, x, y)

	listaAreas.append(imagem)

	return listaAreas

def gerarCampos(screen):
	imgList = []
	imagem = campo("imagens/0.png", 0)
	imgList.append(imagem)
	x = (SCREEN_WIDTH - (imagem.getWidth() * 10)) // 2
	y = SCREEN_HEIGHT - 80
	imagem.setX(x)
	imagem.setY(y)

	x += imagem.getWidth()
	for i in range(1, 10):
		imagem = campo("imagens/"+ str(i) +".png", i, x, y)
		imgList.append(imagem)
		x += imagem.getWidth()
	return imgList

def getImagem():
	global valorRandAnterior

	valor = randint(1, QTD_IMAGENS)
	while(valorRandAnterior == valor):
		valor = randint(1, QTD_IMAGENS)
	valorRandAnterior = valor

	if(valor == 1):
		return "imagens/bolas.png"
	elif(valor == 2):
		return "imagens/flores.png"
	elif(valor == 3):
		return "imagens/morangos.png"
	elif(valor == 4):
		return "imagens/bananas.png"
	elif(valor == 5):
		return "imagens/relogios.png"
	elif(valor == 6):
		return "imagens/xicaras.png"
	elif(valor == 7):
		return "imagens/abelhas.png"
	elif(valor == 8):
		return "imagens/guarda chuvas.png"
	elif(valor == 9):
		return "imagens/chaves.png"
	elif(valor == 10):
		return "imagens/guitarras.png"