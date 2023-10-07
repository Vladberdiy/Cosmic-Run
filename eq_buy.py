from pygame import *
from w_s import WS

class EQ_BY:
	def __init__(self, skin_name):
		self.skin_name = skin_name
		self.data = WS()
		self.prices = self.data.read_skins_price()

		self.skin_price =  self.prices[self.skin_name]
	def return_price(self):
		self.skin_price =  self.prices[self.skin_name]
		return self.skin_price
