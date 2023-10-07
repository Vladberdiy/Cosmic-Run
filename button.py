from pygame import *

class Button:
	def __init__(self, s, c, pos, pos2, w, h, text, c_text, size_text):
		self.size_text = size_text
		self.f1 = font.Font(None, self.size_text)
		self.pos = pos
		self.pos2 = pos2
		self.s = s
		self.c = c
		self.w = w
		self.h = h
		self.rect = Rect((self.pos, self.pos2),(self.w, self.h))
		self.colors = {
			'normal': "#fafafa",
			'hover': "#6e6e6e",
			'pressed': "#181a18"
		}
		self.text = text
		self.c_text = c_text



		draw.rect(self.s ,self.c,[self.pos,self.pos2,self.w,self.h])
		self.s.blit(self.f1.render(self.text, True, self.c_text), (self.rect.x, self.rect.y +5))
	def pressed(self, e, func):
		
		mousePos = mouse.get_pos()
		
		if self.rect.collidepoint(mousePos) :
			if mouse.get_pressed(num_buttons=3)[0]:
				func()
				return True