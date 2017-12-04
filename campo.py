from objeto import *

class campo(objeto):
	def __init__(self, caminhoImagem, idObj, x=None, y=None):
		objeto.__init__(self, caminhoImagem, idObj, x, y)
		self.flagMove = True

	def setFlagMove(self, flagMove):
		self.flagMove = flagMove
	def getFlagMove(self):
		return self.flagMove
	

	def movimentar(self, screen, statusMouse, clock):
		moX,moY = pygame.mouse.get_pos()
		imWidth = self.getWidth()
		imHeight = self.getHeight()
		x = self.getX()
		y = self.getY()

		if(moX > x and moX < imWidth + x and moY > y and moY < imHeight+y):
			self.flagMove = True
		if(not statusMouse[0]):
			self.flagMove = False
		if(self.flagMove):
			idObj = self.idObj
			self.setX(moX - imWidth/2)
			self.setY(moY - imHeight/2)
		return self.flagMove