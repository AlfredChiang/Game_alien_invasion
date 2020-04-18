class GameStats():
	"""跟踪游戏的统计信息"""
	def __init__(self, game_set):
		"""初始化统计信息"""
		self.game_set = game_set
		#在任何情况下都不应重置最高得分
		self.high_score = 0

		self.reset_stats()

		#游戏启动时处于活动状态
		self.game_active = False

	def reset_stats(self):
		"""初始化在游戏运行期间可能变化的统计信息"""
		self.ships_left = self.game_set.ship_limit
		self.score = 0	#每次开始游戏时重置得分
		self.level = 1  #每次开始游戏时重置等级