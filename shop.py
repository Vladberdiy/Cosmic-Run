from pygame import *
from button import Button
from w_s import WS
from change_skin import CS
from eq_buy import EQ_BY
import math


class Shop:
	def __init__(self, win, func):
		self.win = win
		self.func = func
		
		#class
		self.data = WS()
		self.skins = CS()
		
		
		#colors
		self.WHITE = (255,255,255)
		self.GREEN = (41, 122, 0)
		self.BLUE = (13, 24, 184)
		#fonts
		self.fonte = font.Font(None, 70)
		self.coins_font = font.Font(None, 30)
		self.text_font = font.Font(None, 20)
		#coins
		self.coins = int(self.data.load_coin())
		#get skin
		self.skin = image.load(self.skins.skin)
		self.skin = transform.scale(self.skin, (200, 200))
		
		self.prices = EQ_BY(self.skins.get_skin())
		self.equip_btn = Button(self.win, self.WHITE, 380, 600, 60, 40, f"Equip", "#000000", 30)
		self.buy_btn = Button(self.win, self.WHITE, 380, 600, 100, 40, f"Buy: {self.prices.return_price()}", "#000000", 20)
		# bg
		self.clock = time.Clock()
		self.bg_menu = image.load("img/bg_menu.gif").convert()
		self.bg_menu_res = transform.scale(self.bg_menu, (800, 800))
		self.bg_width = 800
		self.FPS = 60
		self.bg_width = 800
		self.scroll_bg = 0
		self.tiles = math.ceil(800/self.bg_width) + 1
	def shop_run(self):
		def passing():
			pass
		self.run_shop = True

		while self.run_shop:
			
			self.clock.tick(self.FPS)
		
			for i in range(0, self.tiles):
				self.win.blit(self.bg_menu_res, (i * self.bg_width + self.scroll_bg, 0))
			
			self.scroll_bg -= 15
			if abs(self.scroll_bg) > self.bg_width:
				self.scroll_bg = 0


			if self.data.load_lang() == "EN":
				self.name_page = self.fonte.render("SHOP", True, self.WHITE)
				self.coins_blit = self.coins_font.render(f"Coin: {self.coins}", True, self.WHITE)
				self.decr_0_skin = self.text_font.render("Bafs: None", True, self.WHITE)
				self.decr_1_skin = self.text_font.render("Bafs: Shield on start", True, self.WHITE)
				self.decr_2_skin = self.text_font.render("Bafs: X2 in start for 600 seconds", True, self.WHITE)
			elif self.data.load_lang() == "UA":
				self.name_page = self.fonte.render("Магазин", True, self.WHITE)
				self.coins_blit = self.coins_font.render(f"Монет: {self.coins}", True, self.WHITE)
				self.decr_0_skin = self.text_font.render("Бафи: Відсутні", True, self.WHITE)
				self.decr_1_skin = self.text_font.render("Бафи: Щит при старті гри", True, self.WHITE)
				self.decr_2_skin = self.text_font.render("Бафи: x2 при старті гри на 600 секунд", True, self.WHITE)
			
			
			if self.skins.get_skin() == "img/player.png":
				self.win.blit(self.decr_0_skin, (300, 200))
			elif self.skins.get_skin() == "img/player1.png":
				self.win.blit(self.decr_1_skin, (300, 200))
			elif self.skins.get_skin() == "img/player2.png":	
				self.win.blit(self.decr_2_skin, (300, 200))
			self.win.blit(self.name_page, (350, 10))
			self.win.blit(self.coins_blit, (0, 100))
			self.win.blit(self.skin, (300, 300))

			self.return_btn = Button(self.win, self.WHITE, 0, 750, 70, 40, "<--", "#000000", 60)
	
			self.plus_btn = Button(self.win, self.WHITE, 100, 400, 50, 40, "<--", "#000000", 60)
			self.minus_btn = Button(self.win, self.WHITE, 600, 400, 50, 40, "-->", "#000000", 60)
			if self.prices.return_price() == 0:
				if self.data.load_lang() == "EN":
					self.equip_btn = Button(self.win, self.WHITE, 380, 600, 60, 40, f"Equip", "#000000", 30)
				elif self.data.load_lang() == "UA":
					self.equip_btn = Button(self.win, self.WHITE, 380, 600, 110, 40, f"Надягнути", "#000000", 30)
			else: 
				if self.data.load_lang() == "EN":
					self.buy_btn = Button(self.win, self.WHITE, 380, 600, 60, 40, f"Buy: {self.prices.return_price()}", "#000000", 30)
				elif self.data.load_lang() == "UA":
					self.buy_btn = Button(self.win, self.WHITE, 380, 600, 100, 40, f"Купити: {self.prices.return_price()}", "#000000", 20)


			for e in event.get():
				if e.type == QUIT:
					self.run_shop = False

				if self.buy_btn.pressed(e, passing):
					if self.data.load_coin() >= self.prices.return_price():
						print(self.skins.get_skin())
						self.bal = self.data.load_coin() - self.prices.return_price()
						self.data.save_all(self.data.load_b_score(), self.bal, self.data.load_lang())
						self.data.buy_skin(self.skins.get_skin())
						self.data = WS()
						self.prices = EQ_BY(self.skins.get_skin())
				if self.equip_btn.pressed(e, passing):
					self.data.save_new_eq_skin(self.skins.get_skin())
				if self.plus_btn.pressed(e, self.skins.plus):
					self.skin = image.load(self.skins.get_skin())
					self.skin = transform.scale(self.skin, (200, 200))
					self.prices = EQ_BY(self.skins.get_skin())
				if self.minus_btn.pressed(e, self.skins.minus):
					self.skin = image.load(self.skins.get_skin())
					self.skin = transform.scale(self.skin, (200, 200))
					self.prices = EQ_BY(self.skins.get_skin())
				if self.return_btn.pressed(e, self.func):
					self.run_shop = False
			display.update()