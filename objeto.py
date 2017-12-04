import pygame

class objeto():
	def __init__(self, caminhoImagem, idObj, x=None, y=None):
		self.iniX = x
		self.iniY = y
		self.x = x
		self.y = y
		self.idObj = idObj;
		self.imagem = pygame.image.load(caminhoImagem)

	def setX(self, x):
		self.x = x
		if(self.iniX == None):
			self.iniX = self.x
	def setY(self, y):
		self.y = y
		if(self.iniY == None):
			self.iniY = self.y
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def getIdObj(self):
		return self.idObj
	def getWidth(self):
		return self.imagem.get_width()
	def getHeight(self):
		return self.imagem.get_height()

	def initPos(self):
		self.x = self.iniX
		self.y = self.iniY

	def clicado(self):
		statusMouse = pygame.mouse.get_pressed()
		moX,moY = pygame.mouse.get_pos()
		imWidth = self.getWidth()
		imHeight = self.getHeight()
		x = self.getX()
		y = self.getY()

		if(statusMouse[0] != 0 and moX > x and moX < imWidth + x and moY > y and moY < imHeight+y):
			return True
		return False

	def renderImagem(self, screen):
		screen.blit(self.imagem, (self.x, self.y))