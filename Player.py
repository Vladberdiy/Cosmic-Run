from pygame import *
from w_s import WS



class Player:
	def __init__(self, win, x, y, color, speed):
		#data
		self.data = WS()
		#init
		self.win = win
		self.x = x
		self.y = y
		self.color = color
		self.speed = speed
		#img
		self.skin = self.data.read_equip_skin()
		self.img = image.load(self.skin).convert_alpha()
		self.img_r = transform. rotate(self.img, 270)
		self.img_rect = self.img_r.get_rect()
		self.rect = Rect(20, 300, self.img_rect.width, self.img_rect.height)
		
		#shield
		self.shield = False
		self.shield_img = image.load("img/shield.png") 
		self.shield_r = transform.rotate(self.shield_img, 270)
		self.shield_img_rect = self.shield_r.get_rect()
		
		#x2
		self.x2_score = False
		self.player_boost = 2
		self.time_score = 0
		self.timex2 =  200

		#player boosts
		if self.skin == "img/player1.png":
			self.shield = True
		if self.skin == "img/player2.png":
			self.timex2 =  600
	def draw_player(self):
		self.win.blit(self.img_r, self.rect)
		if self.shield:
			self.shield_rect = (self.rect.x + 30, self.rect.y, self.shield_img_rect.width, self.shield_img_rect.height)
			self.win.blit(self.shield_r, self.shield_rect)
		if self.x2_score:
			self.time_score += 1
			if self.time_score > self.timex2:
				self.x2_score = False
				self.time_score = 0

	def event_player(self):
		self.keys = key.get_pressed()		
		self.cont = self.data.read_control()
		if self.keys[key.key_code(self.cont["up"])] and self.rect.y > 60:
			self.rect.y -= self.speed
		elif self.keys[key.key_code(self.cont["down"])] and self.rect.y  < 770:
			self.rect.y += self.speed
