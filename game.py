from pygame import *
from button import Button
from settings import Settings
from w_s import WS
import math
from Player import Player
import random as rd
from Enemy import Enemy
from Shield import Shield
from X2 import X2


class Game:
	def __init__(self, win, func):
		# init
		self.win = win
		self.func = func
		#color
		self.WHITE = (255,255,255)
		self.GREEN = (41, 122, 0)
		self.BLUE = (13, 24, 184)
		self.RED = (209, 10, 10)
		# bg
		self.bg_menu = image.load("img/bg_menu.gif")
		self.bg_menu_res = transform.scale(self.bg_menu, (800, 800))
		#time
		self.clock = time.Clock()
		# class
		self.player = Player(self.win, 100, 400, self.GREEN, 10)
		self.enemy = Enemy(self.win, 700, rd.randint(0, 800), rd.randrange(10, 16))
		self.data = WS()
		self.shield = Shield(self.win, 800, rd.randint(100, 800), rd.randrange(7, 9))
		self.x2 = X2(self.win, 800, rd.randint(100, 800), rd.randrange(7, 9))
		# fonts
		self.font = font.Font(None, 30)
		self.font1 = font.Font(None, 70)	
		#score
		self.score_num = 0
	
	def run_game(self):
		self.run_gamee = True
		self.FPS = 60
		self.bg_width = 800
		self.scroll_bg = 0
		self.tiles = math.ceil(800/self.bg_width) + 1
		# main loop
		while self.run_gamee:
			
			self.clock.tick(self.FPS)

			self.enemy.enemy_create()
			self.shield.shield_create()
			self.x2.x2_create()

			self.win.blit(self.bg_menu_res, (0, 0))
			

				
		
			

			for i in range(0, self.tiles):
				self.win.blit(self.bg_menu_res, (i * self.bg_width + self.scroll_bg, 0))
			
			self.scroll_bg -= self.FPS
			if abs(self.scroll_bg) > self.bg_width:
				self.scroll_bg = 0			



			
			self.player.draw_player()
			

			for e in self.enemy.enemy_list:
				e.enemy_draw()
				if e.x < -200:
					self.enemy.enemy_list.pop(0)
					self.score_num += 2 * self.player.player_boost
				if self.player.rect.collidepoint(e.x, e.y):
					if self.player.shield == False:
						if self.score_num > self.data.load_b_score():
							self.data.save_all(self.score_num, self.data.load_coin(), self.data.load_lang())
							self.data = WS()
						else: self.data.save_all(self.data.load_b_score(), self.data.load_coin() + self.score_num / 100, self.data.load_lang())
						self.die = self.font1.render(f'You die', True, self.WHITE)
						self.win.blit(self.die, (300, 300))
						display.update()
						time.wait(2000)
						self.run_gamee = False
						self.func()
					elif self.player.shield == True:
						self.enemy.enemy_list.remove(e)
						self.player.shield = False

			for s in self.shield.shield_list:
				s.shield_draw()
				if s.x < -200:
					self.shield.shield_list.pop(0)
					self.score_num += 5 * self.player.player_boost
				if self.player.rect.collidepoint(s.x, s.y):
					if self.player.shield == False:
						self.shield.shield_list.remove(s)
						self.player.shield = True
					else: pass
			
			for c in self.x2.x2_list:
				c.x2_draw()
				if c.x < -200:
					self.x2.x2_list.pop(0)
					self.score_num += 5 * self.player.player_boost
				if self.player.rect.collidepoint(c.x, c.y):
					if self.player.x2_score == False:
						self.x2.x2_list.remove(c)
						self.player.x2_score = True
					else: pass

			
			self.player.event_player()
			if self.data.load_lang() == "EN":
				self.score_r = self.font.render(f'Score: {self.score_num}', True, self.WHITE)
				self.b_score_r = self.font.render(f'Best Score: {self.data.load_b_score()}', True, self.WHITE)
			elif self.data.load_lang() == "UA":
				self.score_r = self.font.render(f'Бали: {self.score_num}', True, self.WHITE)
				self.b_score_r = self.font.render(f'Рекорд: {self.data.load_b_score()}', True, self.WHITE)
			
			self.time_x2_r = self.font.render(f':  {self.player.timex2 - self.player.time_score}' , True, self.WHITE)
			draw.rect(self.win, (84, 76, 76), (0, 0, 800, 50))
			
			self.win.blit(self.score_r, (0, 15))
			self.win.blit(self.b_score_r, (250, 15))
			if self.player.x2_score:
				self.win.blit(self.x2.img, (550, 0))
				self.win.blit(self.time_x2_r, (600, 0))

			for e in event.get():
				if e.type == QUIT:
					self.run_gamee = False




			display.flip()