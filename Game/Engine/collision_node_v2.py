from .collision_logic_v2 import Collision_Logic_v2

#use this for the games loop collision
class Collision_Node_v2():
	def __init__(self, cLogic, tNode):
		self.__logic = cLogic
		self.__tNode = tNode

		#<--Rosters-->#
		self.__entityRoster = None #All Entities\if move then here.
		self.__staticRoster	= None #Tags that can't move, Exclude Walls
		self.__playerRoster	= None #Player Tags
		self.__weaponRoster	= None #Any Weapons Tags
		self.__enemyRoster	= None #Enemy Tags
		self.__everyRoster	= None #All Tags Roster
		self.__projRoster	= None #Any Flying Tags
		self.__wallRoster	= None #Wall Tags

		#Statics vs. Walls#
		"""Statics can't move alone, Walls can't move period."""

		#<--Collision Results-->#
		self.__cResult = None #Collision
		self.__sResult = None #Side
		self.__wallHit = None


	def Collision_Result(self, cResult, objMain):
		#cResult is a dictionary
		self.__cResult = cResult #List of objects that are colliding with given objMain.
		objList = []


		if objMain.get_isStatic() == True:
			list = []
			# print('getting problems because I am calling to My_Collision twice when unecisary.')
			for obj in self.__cResult:
				if obj.get_groupID() in self.__entityRoster:
					print('entity')
					#if 'friend':
					#	OSC='friend'
					#else:
					#	OSC='enemy'

				elif obj.get_groupID() in self.__wallRoster:
					savedDir = None
					x, y = 0, 0
					# print('wall', obj.get_ID())
					lastDir = objMain.get_lastDirection(opp=True) #opp == opposite
					# print(lastDir)
					direction = self.__logic.Side_Calculation(obj=objMain, target=obj)
					# print(direction)
					#Iterates over a list of the opposite last directions moved
					for dir in lastDir:
						#numbers to compile direction.
						print(dir, 'direction')
						if dir == 'down':
							y+=1
						elif dir == 'up':
							y-=1
						if dir == 'right':
							x+=1
						elif dir == 'left':
							x-=1
						print((x, y), 'tuple')

					var = self.Tuple_Decifer(tuple=(x, y))
					print('<#------------------------------#>')
					objMain.My_Collision(OSC='Static', side=var)

				elif obj.get_groupID() in self.__weaponRoster:
					print('weapon')

				elif obj.get_groupID() in self.__projRoster:
					print('arrow')

				elif obj.get_groupID() in self.__staticRoster:
					print('statics')
		else:
			objMain.My_Collision()
			return


	"""#|----------Extra Functions----------|#"""
	def Tuple_Decifer(self, tuple):
		x, y = tuple
		result = []
		if x > 0:
			result.append('right')
		elif x < 0:
			result.append('left')
		else:
			result.append('nutral')

		if y > 0:
			result.append('down')
		elif y < 0:
			result.append('up')
		else:
			result.append('nutral')
		# print(result, 'result')
		# print('<#------------------------------#>')
		if result[0] != 'nutral' and result[1] == 'nutral':
			print(result[0], 'result')
			return result[0]
		elif result[0] == 'nutral' and result[1] != 'nutral':
			print(result[1], 'result')
			return result[1]



	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	# def get_...


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_entityRoster(self, Roster):
		self.__entityRoster = Roster
		self.__logic.set_entityRoster(Roster)

	def set_playerRoster(self, Roster):
		self.__playerRoster = Roster

	def set_staticRoster(self, Roster):
		self.__staticRoster = Roster

	def set_weaponRoster(self, Roster):
		self.__weaponRoster = Roster

	def set_enemyRoster(self, Roster):
		self.__enemyRoster = Roster

	def set_everyRoster(self, Roster):
		self.__everyRoster = Roster

	def set_projRoster(self, Roster):
		self.__projRoster = Roster

	def set_wallRoster(self, Roster):
		self.__wallRoster = Roster
