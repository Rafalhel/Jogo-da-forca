# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
	x = 0
	tt = 0
	cor = []
	err = []
	# Método Construtor
	def __init__(self, word):
		# Palavra sorteada



		while self.x < 6:
			self.word = word
			self.hi = self.hide_word()
			lt = ",".join((self.cor))
			le = ",".join((self.err))
			print(board[self.x])
			print(self.hi)
			print(f"Letras corretas: {lt}")
			print(f"Letras erradas: {le}")
			self.letter = input("Digite uma letra: ")
			self.guess(self.letter)
			self.print_game_status()
			self.hangman_won()



		
	# Método para adivinhar a letra
	def guess(self, letter):
		zz = 0
		for i in self.word:
			if i == letter:
				zz += 1
			else:
				zz += 0
		if zz >= 1:
			self.cor.append(letter)
			self.tt = 1
		else:
			self.err.append(letter)
			self.tt = 0
			self.x+=1

		# # Letra digitada
		# self.letter = letter
		# z = 0
		# for i in self.word:
		# 	if i == letter:
		# 		z +=1
		# 	else:
		# 		pass
		# if z == 0:
		# 	self.x +=1
		#
		# for i in self.word:
		# 	if letter == i:
		#
		#
		#
		# return board[self.x]



	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if self.x == 6:
			return True
		return False
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if '_' not in self.r:
			self.x = 10
			return True
		return False




	# Método para não mostrar a letra no board
	def hide_word(self):
		p = []
		self.r=''
		for i in self.word:
			if i not in self.cor:
				self.r += '_'
			else:
				self.r += i
			p.append(i)
		palavra = "".join(p)
		return f"Palavra: {self.r}"
		# x = len(self.word)
		# # y = self.word
		# c = []
		# for i in self.word:
		# 	c.append(i)
		# for i in range (0,x):
		# 	if c[i] != lett and c[i] != "_":
		# 		c[i] = "_"
		# 	else:
		# 		self.cor.append(lett)
		# 		c[i] = lett
		# palavra = "".join(c)
		# return palavra


		# if i != y:
		# 	self.word.replace(i,"_")
		# 	print(y)

		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		if self.tt == 1:
			lil = len(self.word)
			pac = 0
			for i in self.word:
				if self.letter == i:
					pac += 1





# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
            bank = f.readlines()
    return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	

	# Verifica o status do jogo
	game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
