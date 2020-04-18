import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
	"""显示得分信息的类"""

	def __init__(self, screen, game_set, stats):
		"""初始化显示得分涉及的属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.game_set = game_set
		self.stats = stats

		#显示得分信息时的字体设置
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		#准备当前得分和最高得分以及等级的图像,剩余飞船数
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		"""将得分转换为一幅渲染的图像"""
		round_score = int(round(self.stats.score, -1))
		score_str = "Score: " + "{:,}".format(round_score)  #字符串格式设置指令
		self.score_image = self.font.render(score_str, True, self.text_color, self.game_set.backgound_color)

		#将得分放在屏幕右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_high_score(self):
		"""将最高分转换为渲染的图像"""
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = "High Score: " + "{:,}".format(high_score)  #字符串格式设置指令
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.game_set.backgound_color)

		#将得分放在屏幕顶部中央
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = 20

	def prep_level(self):
		"""将等级转换为渲染图像"""
		self.level_image = self.font.render("Level: " + str(self.stats.level), True, self.text_color, self.game_set.backgound_color)

		#将等级放在得分下方
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.screen_rect.right - 20
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships(self):
		"""显示还余下多少艘飞船"""
		self.ships = Group()
		#根据玩家还有多少艘飞船运行一个循环相应的次数
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.game_set, self.screen)
			ship.rect.x = 10 + ship.rect.width * ship_number
			ship.rect.y = 10
			self.ships.add(ship)


	def show_score(self):
		"""在屏幕显示当前得分和最高得分"""
		self.screen.blit(self.score_image, self.score_rect) #将得分图像显示到屏幕上，并将其放在score_rect指定位置
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)  #对编组调用draw(),pygame将绘制每艘飞船