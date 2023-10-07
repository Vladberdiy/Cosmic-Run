from w_s import WS

class Change_Lang:
	def __init__(self):
		self.data = WS()
		self.lang = self.data.load_lang()
		self.langs = ["EN", "UA"]
		if self.lang == "EN":
			self.i = 0
		elif self.lang == "UA":
			self.i = 1
	def r_pressed(self):
		for x in self.langs:
			if x != self.lang:
				return  x
				break
	def l_pressed(self):
		if self.i < len(self.langs) and self.i >= 0:
			self.i -= 1
		else: self.i = len(self.langs)
		return self.langs[self.i]


lng = Change_Lang()
print(lng.l_pressed())




