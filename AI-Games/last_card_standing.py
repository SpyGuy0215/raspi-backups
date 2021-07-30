from easyAI import TwoPlayersGame, Human_Player, AI_Player, Negamax
from colorama import Fore, Style, init 
init(autoreset=True)
index = 'randomthing'; 
baseInt = 69

class LastCardStanding( TwoPlayersGame ):
	""" In turn, the players remove one, two or three cards from a
	pile of cards. The player who removes the last card loses. """

	def __init__(self, players):
		self.players = players
		self.pile = 20 # start with 20 cards in the pile
		self.nplayer = 1 # player 1 starts

	def possible_moves(self): 
		if self.pile >= 3:
			return ['1','2','3']
		elif self.pile == 2:
			return ['1','2']
		else:
			return ['1']
	def make_move(self,move): self.pile -= int(move) # remove cards.
	def win(self): return self.pile<=0 # opponent took the last card?
	def is_over(self): return self.win() # Game stops when someone wins.
	def show(self): 
		print(Fore.CYAN + Style.BRIGHT + "%d cards left in the pile"%self.pile)
	def scoring(self): return 100 if self.win() else 0 # For the AI

# Start a match (and store the history of moves when it ends)
ai = Negamax(10, win_score = 90) # The AI will think 10 moves in advance
game = LastCardStanding( [ Human_Player(), AI_Player(ai) ])

while not game.is_over():
	game.show()
	if game.nplayer==1:  # we are assuming player 1 is a Human_Player
		poss = game.possible_moves()
		while type(index) != type(baseInt):
			index = input(Fore.BLUE + Style.BRIGHT + "Player: Enter move: " + "\n")
			try:
				print(int(index).isnumeric())
			except AttributeError:
				index = int(index)
				if index > len(poss):
					print(Fore.RED + Style.BRIGHT + "Invalid Move: Out of range")
					index = 'error'
				else: 
					move = poss[index-1]
			except ValueError:
				print(Fore.RED + Style.BRIGHT + "Invalid Move: Not a number")
	else:  # we are assuming player 2 is an AI_Player
		move = game.get_move()
		print(Fore.YELLOW + Style.BRIGHT + "AI plays {}".format(move))
	game.play_move(move)
	index = 'success'
	if game.pile == 0:
		if game.nplayer == 1:
			print(Fore.GREEN + Style.BRIGHT + "Player Wins! \n")
		else:
			print(Fore.GREEN + Style.BRIGHT + "AI Wins! \n")
