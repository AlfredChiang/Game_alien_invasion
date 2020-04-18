#import sys 
import pygame
from settings import Settings
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
#from alien import Alien
import game_functions as gf
from pygame.sprite import Group
"""pygame.sprite.Group类类似于列表，但提供有助于开发游戏的额外功能"""

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
#	screen = pygame.display.set_mode((700, 520))	#双括号 参数必须是一个二项的序列，而不是整数
	pygame.display.set_caption("Alien Invasion")

	game_set = Settings()	#调用类，自动生成一个设置实例
	screen = pygame.display.set_mode(
		(game_set.screen_width, game_set.screen_hight)
		)  #生成屏幕对象
	play_button = Button(screen, "Play") #创建按钮
	ship = Ship(game_set, screen)	#创建一艘飞船
	bullets = Group()	#创建一个用于存储子弹的编组Group实例
	aliens = Group()    #创建一个外星人编组
	stats = GameStats(game_set) #创建一个用于存储游戏统计信息的实例
	sb = Scoreboard(screen, game_set, stats)  #创建记分牌

	#创建外星人群
	gf.creat_fleet(screen, game_set, ship, aliens)

	while True:
		gf.check_events(play_button, stats, aliens, bullets,
			screen, game_set, ship, sb)

		if stats.game_active:
			ship.update()
	#		bullets.update()
			gf.update_bullets(bullets, aliens, screen, game_set, ship, stats, sb) 
			#当对编组调用update()时，编组将自动对其中的每个sprite(bullet)调用update()
			gf.update_aliens(game_set, aliens, ship, stats, sb, bullets, screen)

		gf.update_screen(game_set, screen, ship, aliens, bullets, stats, play_button, sb)

		#删除已消失的子弹 遍历编组的副本从而可以将消失的子弹全部删除
#		for bullet in bullets.copy():
#			if bullet.rect.bottom <= 0:
#				bullets.remove(bullet)
				#print(len(bullets))

run_game() 




