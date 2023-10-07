from pygame import *
import random as rd

class X2:
	def __init__(self, win, x, y, speed):
		self.win = win
		self.x = x
		self.y = y
		self.speed = speed
		self.img = image.load("img/x2.png").convert_alpha()
		self.x2_img_rect = self.img.get_rect()
		self.rect = Rect(self.x, self.y, self.x2_img_rect.width, self.x2_img_rect.height)
		self.x2_list = []
		self.y_gen = rd.randint(500, 1500)
		self.c = 0
	def x2_draw(self):
		self.x -= self.speed
		self.win.blit(self.img, (self.x, self.y))
	def x2_create(self):
		self.c += 1

		if self.c > self.y_gen:
			self.x2 = X2(self.win, 800, rd.randint(100, 800), rd.randrange(7, 9))
			self.x2_list.append(self.x2)
			self.y_gen += rd.randint(500, 1500)
