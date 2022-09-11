from enum import Enum

class Rank(Enum):
	
	def __lt__(self, other: Rank) -> bool:
		# self.Two = 2 
		# self.Three = 3
		# self.Four = 4
		# self.Five = 5
		# self.Six = 6
		# self.Seven = 7
		# self.Eight = 8
		# self.Nine = 9 
		# self.Ten = 10
		# self.Jack = 11
		# self.Queen = 12
		# self.King = 13 
		# self.Ace = 14

		self.Two = "Two"
		self.Three = "Three"
		self.Four = "Four"
		self.Five = "Five"
		self.Six = "Six"
		self.Seven = "Seven"
		self.Eight = "Eight"
		self.Nine = "Nine"
		self.Ten = "Ten"
		self.Jack = "Jack"
		self.Queen = "Queen"
		self.King = "King"
		self.Ace = "Ace"
		# raise NotImplementedError


card1 = Rank(Two)