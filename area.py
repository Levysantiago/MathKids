"""
	Autor: Levy Santiago
	Última modificação: 04/12/2017
"""

from objeto import *

class area(objeto):
	def __init__(self, caminhoImagem, idObj, x=None, y=None, idCampo=None):
		objeto.__init__(self, caminhoImagem, idCampo, x, y)
		#O id do campo que está nessa area
		self.idCampo = idCampo
		self.vazia = True

	def setIdCampo(self, idCampo):
		self.idCampo = idCampo
		self.vazia = False
	
	def getIdCampo(self):
		return self.idCampo
	
	def ehVazia(self):
		return self.vazia

	def resetar(self):
		self.idCampo = None
		self.vazia = True