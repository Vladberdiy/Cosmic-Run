from pygame import *
from button import Button
from w_s import WS
import keyboard as keyb
class Settings:
	def __init__(self, win, func):
		self.win = win
		self.WHITE = (255,255,255)
		self.GREEN = (41, 122, 0)
		self.BLUE = (13, 24, 184)
		self.func = func
		self.data = WS()
		self.cont = self.data.read_control()
		
	def run_settings(self):
		self.run_settings = True
		self.set_1 = font.Font(None, 70)
		self.set_r_1 = self.set_1.render('SETTINGS', True, self.WHITE)
		self.set_r_2 = self.set_1.render("Налаштування", True, self.WHITE)

		self.lang_list_text = font.Font(None, 40)
		self.lang_r = self.lang_list_text.render("change lang", True, self.WHITE)
		self.lang_r_1 = self.lang_list_text.render("змінити мову", True, self.WHITE)
		self.change_text = self.lang_list_text.render("change control", True, self.WHITE)
		self.change_text_1 = self.lang_list_text.render("змінити керування", True, self.WHITE)
		self.up_txt = self.lang_list_text.render("UP:  ", True, self.WHITE)
		self.up_txt_1 = self.lang_list_text.render("Вгору:  ", True, self.WHITE)
		self.down_txt = self.lang_list_text.render("DOWN:  ", True, self.WHITE)
		self.down_txt_1 = self.lang_list_text.render("Вниз:  ", True, self.WHITE)
		def passing():
			pass
		while self.run_settings:
			for e in event.get():
				if e.type == QUIT:
					self.run_settings = False
			

				self.win.fill((0, 0, 0))
			
			
				if self.data.load_lang() == "EN":
					self.win.blit(self.set_r_1, (275, 50))
					self.win.blit(self.lang_r, (100, 340))
					self.win.blit(self.change_text, (500, 200))
					self.win.blit(self.up_txt, (500, 250))
					self.win.blit(self.down_txt, (500, 300))
				elif self.data.load_lang() == "UA":
					self.win.blit(self.set_r_2, (275, 50))
					self.win.blit(self.lang_r_1, (100, 340))
					self.win.blit(self.change_text_1, (500, 200))
					self.win.blit(self.up_txt_1, (500, 250))
					self.win.blit(self.down_txt_1, (500, 300))

	
				

				self.up_btn = Button(self.win, self.WHITE, 600, 250, 100,40, self.cont["up"], "#000000", 40)
				self.down_btn = Button(self.win, self.WHITE, 600, 300, 100,40, self.cont["down"], "#000000", 40)
				self.eng_btn = Button(self.win, self.WHITE, 100, 375, 70,40, "EN", "#000000", 40)
				self.ua_btn = Button(self.win, self.WHITE, 100, 425, 70, 40, "UA", "#000000", 40)
				self.return_btn = Button(self.win, self.WHITE, 0, 750, 70, 40, "<--", "#000000", 60)

				if self.down_btn.pressed(e, passing):
					self.name = keyb.read_key()
					self.data.save_cont(self.cont['up'], self.name)
					self.cont =  self.data.read_control()
				if self.up_btn.pressed(e, passing):
					self.name = keyb.read_key()
					self.data.save_cont(self.name, self.cont['down'])
					self.cont =  self.data.read_control()
				if self.eng_btn.pressed(e, passing):
					self.data.save_all(self.data.load_b_score(), self.data.load_coin(), "EN")
					self.data = WS()
				if self.ua_btn.pressed(e, passing):
					self.data.save_all(self.data.load_b_score(),self.data.load_coin(), "UA")
					self.data = WS()
				if self.return_btn.pressed(e, self.func):
					self.run_settings = False
				display.flip()

