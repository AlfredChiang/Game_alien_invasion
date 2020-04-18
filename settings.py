class Settings():
	"""docstring for Settings"""
	
	def __init__(self):
		"""初始化游戏的静态设置"""

		#屏幕设置
		self.screen_width = 1200
		self.screen_hight = 800
		self.backgound_color = (230, 233, 230) 

		#飞船的设置
#		self.ship_speed_factor = 3.3
		self.ship_limit = 2

		#子弹设置
#		self.bullet_speed_factor = 7
		self.bullet_width = 3
		self.bullet_hight = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_allowed = 5

		#alien设置
#		self.alien_speed_factor = 1
#		self.fleet_drop_speed = 50
		#fleet_direction为1表示右移，为-1表示像左移
#		self.fleet_direction = 1

		#以怎样的速度加快游戏节奏
		self.alien_speedup_scale = 1.1
		#外星人点数的提高速度
		self.score_scale = 1.5
		#初始化游戏动态设置
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""初始化动态设置"""
		self.ship_speed_factor = 5.2
		self.bullet_speed_factor = 7
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		#fleet_direction为1表示右移，为-1表示像左移
		self.fleet_direction = 1
		#记分
		self.alien_points = 50

	def increase_speed(self):
		self.ship_speed_factor *= self.alien_speedup_scale
		self.bullet_speed_factor *= self.alien_speedup_scale
		self.alien_speed_factor *= self.alien_speedup_scale
		self.fleet_drop_speed *= self.alien_speedup_scale
		#为了让点数为整数 self.score_scale为浮点型
		self.alien_points = int(self.alien_points * self.score_scale) 
#		print(self.alien_points)
		