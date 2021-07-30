from easyAI import TwoPlayersGame, AI_Player, Negamax
from easyAI.Player import Human_Player
from colorama import Fore, Style,  init 
init(autoreset=True)

class TicTacToe(TwoPlayersGame):
	def __init__(self, players):
		self.players = players
		self.nplayer = 1
		self.board = [0] * 9
		print(self.board)
	def possible_moves(self):
		return[a + 1 for a, b in enumerate(self.board) if b == 0]
	def make_move(self, move):
		self.board[int(move) - 1] = self.nplayer
	def loss_condition(self):
		possible_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
		return any([all([(self.board[i-1] == self.nopponent)for i in combination])for combination in possible_combinations])
	def is_over(self):
		return(self.possible_moves() == []) or self.loss_condition()
	def show(self):
		print('\n'+'\n'.join([' '.join([[Fore.WHITE + Style.BRIGHT + '.', Fore.BLUE + Style.BRIGHT + 'O', Fore.RED + Style.BRIGHT + 'X'][self.board[3*j + i]] 
				for i in range(3)]) for j in range(3)])) 
	def scoring(self):
		return 100 if self.loss_condition() == False else 0
ai = Negamax(20)
TicTacToe([Human_Player(),AI_Player(ai) ]).play()

