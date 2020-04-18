import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""继承导入的父类Sprite，子类Bullet将自动获得父类的所有属性和方法"""
	def __init__(self, game_set, screen, ship):
		"""初始化父类属性，接受创建父类实例所需的信息"""
		super().__init__()
		"""关联函数，让子类包含父类的所有属性"""
		self.screen = screen

		#先在(0,0)处创建一个表示子弹的矩形，然后再设置正确的位置
		self.rect = pygame.Rect(0, 0, game_set.bullet_width,
			game_set.bullet_hight)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#存储用小数表示的子弹y坐标
		self.y = float(self.rect.y)

		self.color = game_set.bullet_color
		self.speed_factor = game_set.bullet_speed_factor

	def update(self):
		"""向上移动子弹"""
		#更新表示子弹位置的小数值
		self.y -= self.speed_factor
		#更新表示子弹位置的rect位置
		self.rect.y = self.y
		#self.rect.y将只存储self.y的整数部分，但对显示子弹而言问题不大

	def draw_bullet(self):
		"""在屏幕绘制子弹"""
		pygame.draw.rect(self.screen, self.color, self.rect)

