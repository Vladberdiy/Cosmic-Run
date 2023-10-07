from pygame import *
from w_s import WS


class CS:
	def __init__(self):
		self.skins = ["img/player.png", "img/player1.png", "img/player2.png"]
		self.i = 0
		self.skin = self.skins[self.i]
		self.data = WS()
	def plus(self):
		self.i += 1
		self.i = self.i % len(self.skins)
	def minus(self):
		self.i -= 1
		self.i = self.i % len(self.skins)
	def get_skin(self):
		return self.skins[self.i]