from pygame import *
from button import Button
from settings import Settings
from w_s import WS
from game import Game
import math
from shop import Shop


WHITE = (255,255,255)
GREEN = (41, 122, 0)
BLUE = (13, 24, 184)
sc_width = 800
sc_height = 800

win = display.set_mode((sc_width, sc_height), HWSURFACE | DOUBLEBUF)
clock = time.Clock()



def game():
	game_init = Game(win, run_menu)
	game_init.run_game()
def shop():
	shop_init = Shop(win, run_menu)
	shop_init.shop_run()
def settings():
	settings_init = Settings(win, run_menu)
	settings_init.run_settings()

def run_menu():

	global WHITE
	global GREEN
	global BLUE
	
	global win 
	global clock
	global lang



	FPS = 60
	run_menuu = True
	win = display.set_mode((800, 800))
	clock = time.Clock()
	data = WS()


	#game name
	game_name_1 = font.Font("font/game_name.ttf", 60)
	game_name_2 = font.Font("font/game_name.ttf", 45)
	game_name_r_1 = game_name_1.render('Cosmic', True, GREEN)
	game_name_r_2 = game_name_2.render('Run', True, GREEN)
	#bg
	bg_menu = image.load("img/bg_menu.gif").convert()
	bg_menu_res = transform.scale(bg_menu, (800, 800))
	bg_width = 800



	#bg animation
	FPS = 60
	bg_width = 800
	scroll_bg = 0
	tiles = math.ceil(sc_width/bg_width) + 1
	while run_menuu:
		clock.tick(FPS)
		
		for i in range(0, tiles):
			win.blit(bg_menu_res, (i * bg_width + scroll_bg, 0))
			
		scroll_bg -= 15
		if abs(scroll_bg) > bg_width:
			scroll_bg = 0

		win.blit(game_name_r_1, (300, 25))
		win.blit(game_name_r_2,(325, 100))


			
		if data.load_lang() == "EN":
			start_btn = Button(win, WHITE, 350, 300, 100, 40, "START", "#000000", 45)
			shop_btn = Button(win, WHITE, 350, 400, 100, 40, "SHOP", "#000000", 45)
			settings_btn = Button(win, WHITE, 325, 500, 150, 40, "SETTINGS", "#000000", 45)
		elif data.load_lang() == "UA":
			start_btn = Button(win, WHITE, 350, 300, 100, 40, "СТАРТ", "#000000", 45)
			shop_btn = Button(win, WHITE, 320, 400, 150, 40, "МАГАЗИН", "#000000", 45)
			settings_btn = Button(win, WHITE, 275, 500, 250, 40, "НАЛАШТУВННЯ", "#000000", 45)
		

		for e in event.get():
			if e.type == QUIT:
				run_menuu = False
			
	


			



			


			if start_btn.pressed(e, game):
				run_menuu = False
			if shop_btn.pressed(e, shop):
				run_menuu = False
			if settings_btn.pressed(e, settings):
				run_menuu = False
			
		display.flip()



if __name__ == '__main__':
	init()
	run_menu()