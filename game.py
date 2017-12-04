from campo import *
from sympy import sqrt
from area import *
from objeto import *
from imgBiblioteca import *

class game():
	def __init__(self, screen, valClock):
		#Quantidade maxima para poder gerar as imagens
		self.qtdMaxGenImagens = 10

		#Limite de pontos
		self.limitePontos = 5

		#Quantidade de repetição de imagens (RESPOSTA FINAL)
		self.qtdImagens = randint(1, self.qtdMaxGenImagens)
		self.qtdAnterior = self.qtdImagens

		#Obtendo uma imagem aleatória
		self.strImgName = getImagem()

		#Lista de números/campos para a escolha da resposta
		self.listaCampos = gerarCampos(screen)

		#Lista para verificação do movimento de cada campo
		self.carregando = [False, -1]

		#Lista das areas onde serão inseridos os numeros
		self.listaAreas = gerarAreas(screen)

		#Botao confirmar
		self.botaoConfirma = objeto("imagens/next.png", 12, SCREEN_WIDTH - 80, SCREEN_HEIGHT/2 - 30)

		#Botao Reset
		self.botaoReset = objeto("imagens/reset.png", 12, SCREEN_WIDTH/2 - 25, SCREEN_HEIGHT/2 + 20)

		#Resultado
		self.certo = objeto("imagens/certo.png", 13)
		self.certo.setX((SCREEN_WIDTH - self.certo.getWidth())/2)
		self.certo.setY((SCREEN_HEIGHT - self.certo.getHeight())/2)
		self.errado = objeto("imagens/errado2.png", 14)
		self.errado.setX((SCREEN_WIDTH - self.errado.getWidth())/2)
		self.errado.setY((SCREEN_HEIGHT - self.errado.getHeight())/2)

		#Boolean para pausar o jogo
		self.pause = False

		#Delay
		self.delay = 0

		#Definindo o FPS 
		self.clock = pygame.time.Clock()
		self.clock.tick(valClock)

		#Pontos
		self.countPontos = 0

		#Fim de jogo
		self.boolFimJogo = False

		#fonte
		self.fonte = pygame.font.Font("fonte/ComicSans.ttf", 25)
		self.fonte2 = pygame.font.Font("fonte/ComicSans.ttf", 20)

		#Textos
		tmp = self.strImgName.split("imagens/")[1]
		tmp = tmp.split(".png")[0]
		self.informacao = self.fonte.render("Informe a quantidade de " + tmp +":", True, (0, 0, 0))
		self.pontosTxt = self.fonte.render("Pontos: ", True, (255, 0, 0))
		self.valPontosTxt = self.fonte.render(str(self.countPontos), True, (255, 0, 0))
		self.respostaTxt = self.fonte.render("Resposta Correta: " + str(self.qtdImagens), True, (0, 0, 0))
		self.corretoTxt = self.fonte.render("Você acertou!", True, (0, 255, 0))

		#Texto Fim de Jogo
		self.botaoResetTxt = self.fonte2.render("Reiniciar Jogo?", True, (0, 0, 0))
		self.textoFinal = self.fonte.render("Fim de Jogo.", True, (0, 0, 0))
		self.informacaoFinal = self.fonte.render("Continue treinando, está cada vez melhor!", True, (0, 0, 0))

	def renderGame(self, screen, corTela):		
		if(not self.pause and not self.boolFimJogo):		
			screen.fill(corTela)

			screen.blit(self.valPontosTxt, (125, 70))

			screen.blit(self.pontosTxt, (20, 70))

			screen.blit(self.informacao, (self.pontosTxt.get_width() + 40, 10))

			multiplicarImagem(screen, self.strImgName, self.qtdImagens)

			self.botaoConfirma.renderImagem(screen)
			
			self.renderCampos(screen)

			#Se o botao for clicado
			if(self.botaoConfirma.clicado() and not self.carregando[0]):
				self.pause = True
				if(self.respostaJogador() == self.qtdImagens):
					self.certo.renderImagem(screen)
					self.countPontos += 1
					self.valPontosTxt = self.fonte.render(str(self.countPontos), True, (255, 0, 0))
					screen.blit(self.corretoTxt, ((SCREEN_WIDTH - self.corretoTxt.get_width())/2, SCREEN_HEIGHT - self.certo.getWidth()/2 -30))
					if(self.countPontos == self.limitePontos):
						self.boolFimJogo = True
				else:
					self.errado.renderImagem(screen)
					self.respostaTxt = self.fonte.render("Resposta Correta: " + str(self.qtdImagens), True, (255, 0, 0))
					screen.blit(self.respostaTxt, ((SCREEN_WIDTH - self.respostaTxt.get_width())/2, SCREEN_HEIGHT - self.errado.getWidth()/2 -30))
		if(self.pause and not self.boolFimJogo):
			self.delay += 1
			if(self.delay == 4000):
				self.resetar()
				self.pause = False

		if(self.boolFimJogo):
			self.fimDeJogo(screen, corTela)

	def fimDeJogo(self, screen, corTela):
		screen.fill(corTela)

		screen.blit(self.textoFinal, ((SCREEN_WIDTH - self.textoFinal.get_width())/2, 70))
		screen.blit(self.informacaoFinal, ((SCREEN_WIDTH - self.informacaoFinal.get_width())/2, 150))
		screen.blit(self.botaoResetTxt, ((SCREEN_WIDTH - self.botaoResetTxt.get_width())/2, 230))
		self.botaoReset.renderImagem(screen)

		if(self.botaoReset.clicado()):
			#Resetando o jogo inteiro
			self.countPontos = 0
			self.valPontosTxt = self.fonte.render(str(self.countPontos), True, (255, 0, 0))
			self.pause = False
			self.boolFimJogo = False
			self.resetar()

	def resetar(self):
		size = len(self.listaCampos)
		for i in range(0, size):
			self.listaCampos[i].initPos()
		
		#Reiniciando o delay
		self.delay = 0
		
		#Resetando a quantidade de repetição de imagens
		self.qtdImagens = randint(1, self.qtdMaxGenImagens)

		#Se a quantidade for a mesma da anterior
		while(self.qtdAnterior == self.qtdImagens):
			self.qtdImagens = randint(1, self.qtdMaxGenImagens)
		self.qtdAnterior = self.qtdImagens
		
		#Atualizando a imagem
		self.strImgName = getImagem()
		tmp = self.strImgName.split("imagens/")[1]
		tmp = tmp.split(".png")[0]
		self.informacao = self.fonte.render("Informe a quantidade de " + tmp +":", True, (0, 0, 0))

	def validaAreas():
		if(self.listaAreas[0] != None and listaAreas[1] != None):
			return False
		return True

	def renderCampos(self, screen):
		size = len(self.listaAreas)
		for i in range(0, size):
			self.listaAreas[i].renderImagem(screen)

		size = len(self.listaCampos)
		for i in range(0, size):
			self.listaCampos[i].renderImagem(screen)
			statusMouse = pygame.mouse.get_pressed()			

			self.definePos(self.listaCampos[i])

			idObj = self.listaCampos[i].getIdObj()
			if(not self.carregando[0] or (self.carregando[0] and self.carregando[1] == idObj)):
				self.carregando[0] = self.listaCampos[i].movimentar(screen, statusMouse, self.clock)
				self.carregando[1] = idObj


	def definePos(self, campo):
		size = len(self.listaAreas)
		atualiza = True

		# Se o campo já estiver na area, ele fica la
		for i in range(0, size):
			if(self.mesmaPos(campo, self.listaAreas[i])):
				atualiza = False
				break

		# Se o campo nao estiver na area, é preciso atualizar x e y
		if(atualiza):
			for i in range(0, size):
				dist = self.distCampos(campo, self.listaAreas[i])
				if(dist > 20):
					if(self.listaAreas[i].getIdCampo() == campo.getIdObj()):
						self.desgrudarAreaCampo(self.listaAreas[i], campo)
				elif(self.listaAreas[i].ehVazia() or (not self.listaAreas[i].ehVazia() and self.listaAreas[i].getIdCampo() == campo.getIdObj())):
					self.grudarAreaCampo(self.listaAreas[i], campo)
					break			
			else:
				campo.initPos()

	def grudarAreaCampo(self, area, campo):
		campo.setX(area.getX())
		campo.setY(area.getY())
		area.setIdCampo(campo.getIdObj())

	def desgrudarAreaCampo(self, area, campo):
		campo.initPos()
		area.resetar()

	def mesmaPos(self, campoA, campoB):
		flag = True
		if(campoA.getX() != campoB.getX()):
			flag = False
		if(campoA.getY() != campoB.getY()):
			flag = False
		return flag

	def distCampos(self, campoA, campoB):
		#Distancia entre pontos
		dist = sqrt((campoB.getX() - campoA.getX())**2 + (campoB.getY() - campoA.getY())**2)
		return dist

	def respostaJogador(self):
		resp = 0

		valArea1 = self.listaAreas[0].getIdCampo()
		valArea2 = self.listaAreas[1].getIdCampo()

		if(valArea2 != None):
			resp += valArea2
			if(valArea1 != None):
				resp += valArea1 * 10
		elif(valArea1 != None):
			resp += valArea1

		return resp
