import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, game_set, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		#向右移动飞船
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		#向左移动飞船
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(game_set, screen, ship, bullets)
#		if len(bullets) < game_set.bullet_allowed: 
#			new_bullet = Bullet(game_set, screen, ship)
			#玩家按空格键时创建一颗新子弹（一个名为new_bullet的实例）
#			bullets.add(new_bullet)	
			#函数gf.check_events(ship，bullets)在子弹实例后面，可以直接调用
	elif event.key == pygame.K_q:
		sys.exit()  

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
	    #向右移动飞船
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		#向右移动飞船
		ship.moving_left = False

def check_events(play_button, stats, aliens, bullets,
			screen, game_set, ship, sb):
	"""响应按键和鼠标事件,无需任何形参"""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event, game_set, screen, ship, bullets)

			elif event.type == pygame.KEYUP:
				check_keyup_events(event, ship)

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				check_play_button(play_button, mouse_x, mouse_y, stats, aliens, bullets,
					screen, game_set, ship, sb)

def check_play_button(play_button, mouse_x, mouse_y, stats, aliens, bullets,
		screen, game_set, ship, sb):
	"""单击play按钮时开始新游戏"""
	if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
		#检查鼠标单击的位置是否在play按钮的rect内, 仅当stats.game_active为false才重新开始
		game_set.initialize_dynamic_settings()  #重置游戏设置为初始值
		pygame.mouse.set_visible(False) #隐藏光标
		stats.reset_stats()
		stats.game_active = True

		#重置记分牌图像
		sb.prep_score()
		sb.prep_level()
		sb.prep_high_score()
		sb.prep_ships()

		#清空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()

		#创建一群新的外星人并让飞船居中
		creat_fleet(screen, game_set, ship, aliens)
		ship.center_ship()


def update_screen(game_set, screen, ship, aliens, bullets, stats, play_button, sb):
	screen.fill(game_set.backgound_color)	#设置背景色
	for bullet in bullets.sprites():
		#方法bullets.sprites()可返回一个列表，包含编组bullets中所有精灵
		bullet.draw_bullet()
	ship.blitme()	#在指定位置绘制飞船	
	aliens.draw(screen)  #在屏幕上绘制编组中每个alien，绘制的位置由元素的属性rect决定
	sb.show_score()

	#如果游戏处于非活动状态，就显示play按钮
	if stats.game_active == False:
		play_button.draw_button()

	pygame.display.flip()	#让最近绘制的屏幕可见

def update_bullets(bullets, aliens, screen, game_set, ship, stats, sb):
	"""更新子弹的位置，并删除已消失的子弹"""
	bullets.update()

	for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
				#print(len(bullets))
	check_bullet_alien_collision(bullets, aliens, screen, game_set, ship, stats, sb)

def check_bullet_alien_collision(bullets, aliens, screen, game_set, ship, stats, sb):
	#检查是否有子弹击中了外星人，如果有，就删除相应的子弹和外星人
	collision = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if collision:
		#检查collision字典是否存在
		for aliens in collision.values():
			#与每颗子弹相关的值都是一个列表aliens
			stats.score += game_set.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats, sb)

	if len(aliens) == 0:
		bullets.empty()
		game_set.increase_speed()

		#提高等级
		stats.level += 1
		sb.prep_level()

		creat_fleet(screen, game_set, ship, aliens)

def check_high_score(stats, sb):
	"""检查是否诞生了最高得分"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()

def fire_bullet(game_set, screen, ship, bullets):
	if len(bullets) < game_set.bullet_allowed: 
		new_bullet = Bullet(game_set, screen, ship)
		#玩家按空格键时创建一颗新子弹（一个名为new_bullet的实例）
		bullets.add(new_bullet)	
		#函数gf.check_events(ship，bullets)在子弹实例后面，可以直接调用  

def get_number_rows(game_set, ship_height, alien_height):
	"""计算屏幕可以容纳多少行外星人"""
	available_space_y = (game_set.screen_hight - ship_height - (3 * alien_height))
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def get_number_aliens(game_set, alien_width):
	"""计算每行可容纳多少个外星人"""
	available_space_x = game_set.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def create_alien(screen, game_set, aliens, alien_number, row_number):
	"""创建一个外星人并将其放在当前行"""
	alien = Alien(screen, game_set)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x

	alien_height = alien.rect.height
	alien.y = alien_height + 2 * alien_height * row_number
	alien.rect.y = alien.y
	aliens.add(alien)

def creat_fleet(screen, game_set, ship, aliens):
	"""创建外星人群"""
	alien = Alien(screen, game_set)
	number_aliens_x = get_number_aliens(game_set, alien.rect.width)
	number_rows = get_number_rows(game_set, ship.rect.height, alien.rect.height)

	#创建外星人群
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			#创建一个外星人并将其加入当前行,从零数到要创建的外星人数
			#将一行外星人加入列
			create_alien(screen, game_set, aliens, alien_number, row_number)

def check_fleet_edges(game_set, aliens):
	"""有外星人到达边缘时采取相应措施"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(game_set, aliens)
			break

def change_fleet_direction(game_set, aliens):
	"""将整群外星人下移，并改变他们的方向"""
	game_set.fleet_direction *= -1
	for alien in aliens.sprites():
		alien.rect.y += game_set.fleet_drop_speed

def ship_hit(stats, sb, aliens, bullets, screen, game_set, ship):
	"""响应被外星人撞到的飞船"""
	#将ship_left减1
	if stats.ships_left > 0:
		stats.ships_left -= 1
		#更新飞船数
		sb.prep_ships()

		#清空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()

		#创建一群新的外星人并将飞船放到屏幕底端中央
		creat_fleet(screen, game_set, ship, aliens)
		ship.center_ship()
	
		#暂停0.5s
		sleep(1)

	else:
		stats.game_active = False
		pygame.mouse.set_visible(True) #显示光标

def check_aliens_bottom(stats, sb, aliens, bullets, screen, game_set, ship):
	"""检查是否有外星人到达屏幕底端"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			#像飞船被撞一样处理
			ship_hit(stats, sb, aliens, bullets, screen, game_set, ship)
			break

def update_aliens(game_set, aliens, ship, stats, sb, bullets, screen):
	"""更新外星人群中所有外星人的位置"""
	check_fleet_edges(game_set, aliens)
	aliens.update()

	#检测外星人与飞船之间的碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(stats, sb, aliens, bullets, screen, game_set, ship)
	#检查是否有外星人到达屏幕底端
	check_aliens_bottom(stats, sb, aliens, bullets, screen, game_set, ship)
