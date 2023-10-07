from pygame import *
import random as rd

class Shield:
	def __init__(self, win, x, y, speed):
		self.win = win
		self.x = x
		self.y = y
		self.speed = speed
		self.img = image.load("img/shield_spawn.png").convert_alpha()
		self.shield_img_rect = self.img.get_rect()
		self.rect = Rect(self.x, self.y, self.shield_img_rect.width, self.shield_img_rect.height)
		self.shield_list = []
		self.y_gen = rd.randint(500, 1000)
		self.c = 0
	def shield_draw(self):
		self.x -= self.speed
		self.win.blit(self.img, (self.x, self.y))
	def shield_create(self):
		self.c += 1

		if self.c > self.y_gen:
			self.shild = Shield(self.win, 800, rd.randint(100, 800), rd.randrange(7, 9))
			self.shield_list.append(self.shild)
			self.y_gen += rd.randint(500, 1000)