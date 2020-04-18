import pygame
from pygame.sprite import Sprite 

class Ship(Sprite):
	"""docstring for Ship"""
	def __init__(self, game_set, screen):
		"""初始化飞船并设置要将飞船绘制到什么地方"""
		super().__init__()
		self.screen = screen
		self.game_set = game_set

	#加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
	#表示图像的矩形，表示屏幕的矩形
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

	#将每艘飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		"""飞船矩形中心的x坐标 = 屏幕矩形中心的x坐标"""
		self.rect.bottom = self.screen_rect.bottom
		"""飞船矩形底部y坐标 = 屏幕矩形底部y坐标"""

		#在飞船属性center中存储小数值
		self.center = float(self.rect.centerx)

		#移动标志
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""根据移动标志调整飞船位置, 保证飞船外接矩形不超屏幕边界"""
		if self.moving_right == True and self.rect.right < self.screen_rect.right:
			self.center += self.game_set.ship_speed_factor
		if self.moving_left == True and self.rect.left > 0:
			self.center -= self.game_set.ship_speed_factor
		#根据self.center再更新rect矩形对象的x坐标
		self.rect.centerx = self.center

	def center_ship(self):
		"""让飞船在屏幕上居中"""
		self.center = self.screen_rect.centerx

	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)
