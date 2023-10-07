from pygame import *
import random as rd

class Enemy():
	def __init__(self, win, x, y, speed):
		self.x = x
		self.y = y
		self.rand_num = rd.randrange(1, 4)
		if self.rand_num == 1:
			self.img = image.load("img/enemy1.png").convert_alpha()
		elif self.rand_num  == 2:
			self.img = image.load("img/enemy2.png").convert_alpha()
		elif self.rand_num == 3:
			self.img = image.load("img/enemy3.png").convert_alpha()
		self.img_rect = self.img.get_rect()
		self.rect = Rect(self.x, self.y, self.img_rect.width, self.img_rect.height)
		self.win = win
		self.y_gen = 10
		self.c = 0
		self.enemy_list = []
		self.speed = speed
	def enemy_create(self):
		self.c += 1
			
		if self.c > self.y_gen:
			self.enemys = Enemy(self.win, 800, rd.randint(100, 800), rd.randrange(10, 16))
			self.enemy_list.append(self.enemys)
			self.y_gen += 10

	
	def enemy_draw(self):
		self.x -= self.speed
		self.win.blit(self.img, (self.x, self.y))

