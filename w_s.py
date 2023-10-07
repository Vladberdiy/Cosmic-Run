import json

class WS:
	def __init__(self):
		with open('json/save.json', 'r+') as f:
			self.data = json.loads(f.read())
	#load lang, coin, b_score
	def load_lang(self):
		self.lang = self.data['lang']
		return self.lang
	def load_coin(self):
		self.coins = self.data['coin']
		return self.coins
	def load_b_score(self):
		self.b_score = self.data['best_score']
		return self.b_score
	#save lang, coin. b_score
	def save_all(self, best_score, coins_new, lang_now):
		self.lang_now = lang_now
		self.best_score = best_score
		self.coins_new = coins_new
		to_json = {"lang": self.lang_now, "coin": self.coins_new, "best_score": self.best_score}
		with open('json/save.json', 'w') as f:
			json.dump(to_json, f)
	#control
	def read_control(self):
		with open('json/control.json', 'r+') as l:
			self.cont = json.loads(l.read())
		return self.cont
	def save_cont(self, up, down):
		self.up_n = up
		self.down_n = down
		to_json = {"up" : self.up_n, "down": self.down_n}
		with open('json/control.json', 'w') as f:
			json.dump(to_json, f)
	#skins
	def read_equip_skin(self):
		with open('json/skin.json', 'r+') as n:
			self.e_skin = json.loads(n.read())
		return self.e_skin["skin_equip"]
	def save_new_eq_skin(self, new_skin):
		self.new_skin = new_skin
		to_json = {"skin_equip" : self.new_skin}
		with open('json/skin.json', 'w') as f:
			json.dump(to_json, f)
	def read_skins_price(self):
		with open('json/skins_price.json', 'r+') as p:
			self.p_skin = json.loads(p.read())
		return self.p_skin
	def buy_skin(self, skin_name):
		self.skin_name = skin_name
		with open('json/skins_price.json', 'r+') as p:
			self.skines = json.loads(p.read())
		
		if self.skin_name in self.skines:
			self.skines[self.skin_name] = 0

		with open('json/skins_price.json', 'w') as file:
			json.dump(self.skines, file)
	def load_up(self):
		self.up = self.cont['up']
		return self.up
	def load_down(self):
		self.down = self.cont['down']
		return self.down



