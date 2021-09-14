import random

moves = ['a','w','d','s']
coinsCount = 20

def initializeBoard():
	board = [['.' for y in range(0,35)] for x in range(0,15)]

	board[7][19] = 'P'
	board[12][7] = 'G'

	for x in range(20):
		while 1:
			r = random.randint(0,14)
			c = random.randint(0,34)
			if board[r][c] == '.':
				board[r][c] = 'C'
				break

	for y in range(30):
		while 1:
			r = random.randint(0,14)
			c = random.randint(0,34)
			if board[r][c] == '.':
				board[r][c] = 'X'
				break
	return board

def showBoard(board):
	for x in range(15):
			for y in range(35):
				print board[x][y],
			print

def gameOver(score):
	print "Game Over !!!"
	print "Final Score is : %d" % score

class Person(object):
	"""docstring for Person"""

	def __init__(self, x, y):
		super(Person, self).__init__()
		self.new_x = self.x = x
		self.new_y = self.y = y

	def makeMove(self, move):
		if move == 'a':
			self.new_y = self.y - 1
		elif move == 's':
			self.new_x = self.x + 1
		elif move == 'w':
			self.new_x = self.x - 1
		elif move == 'd':
			self.new_y = self.y + 1
		self.new_x = self.new_x%15
		self.new_y = self.new_y%35

	def checkWall(self, board):
		if board[self.new_x][self.new_y] == 'X':
			return 1
		return 0

	def checkCoin(self, board):
		if board[self.new_x][self.new_y] == 'C':
			return 1
		return 0

class Pacman(Person):

	def __init__(self,x,y):
		Person.__init__(self,x,y)
		self.score = 0

	def checkGhost(self,board):
		if board[self.new_x][self.new_y] == 'G':
			return 1
		return 0

	def collectCoin(self,board):
		board[self.new_x][self.new_y] = '.'
		self.score += 1

	def updatePosition(self,board):
		if board[self.new_x][self.new_y] == 'X':
			self.new_x = self.x
			self.new_y = self.y
			return
		board[self.x][self.y] = '.'
		board[self.new_x][self.new_y] = 'P'
		self.x = self.new_x
		self.y = self.new_y

class Ghost(Person):
	
	def __init__(self,x,y):
		Person.__init__(self,x,y)
		self.flag = 0

	def checkPlayer(self,board) :
		if board[self.new_x][self.new_y] == 'P':
			return 1
		return 0

	def updatePosition(self,board):
		if self.flag == 1:
			board[self.x][self.y] = 'C'
		else:
			board[self.x][self.y] = '.'
		self.x = self.new_x
		self.y = self.new_y
		board[self.x][self.y] = 'G'

if __name__ == '__main__':

	board = initializeBoard()
	player = Pacman(7,19)
	ghost = Ghost(12,7)

	while 1:
		showBoard(board)
		move = raw_input("Enter your move : ")
		if move == 'q' :
			gameOver(player.score)
			break
		elif move not in moves :
			print "Move not recognized"
			continue
		else :
			player.makeMove(move)
			if player.checkGhost(board) :
				gameOver(player.score)
				break
			elif player.checkCoin(board) :
				player.collectCoin(board)
				if player.score == coinsCount :
					gameOver(player.score)
					break

			player.updatePosition(board)

			move = moves[random.randint(0,3)]
			ghost.makeMove(move)

			if ghost.checkPlayer(board) :
				gameOver(player.score)
				break
			elif ghost.checkCoin(board) :
				ghost.flag = 1
				continue
			elif ghost.checkWall(board) :
				continue
			ghost.updatePosition(board)
