from .collision_logic_v2 import Collision_Logic_v2
# from intertools import cycle
from itertools import cycle

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
		"""Statics can be manipulated and moved by player or other, walls don't get moved by anything."""

		#<--Collision Results-->#
		self.__cResult = None #Collision
		self.__sResult = None #Side
		self.__wallHit = None


	def Collision_Result(self, cResult, objMain):
		#cResult is a dictionary
		self.__cResult = cResult #List of objects that are colliding with given objMain.
		objCount = 0
		listOSC	 = []
		listDIR	 = []


		if len(self.__cResult) >= 2: #this probably isn't needed
			pass #for now

		if objMain.get_isStatic() == True:
			# print('getting problems because I am calling to My_Collision twice when unecisary.')
			for obj in self.__cResult:
				objCount += 1
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
						# print('pushing:', dir)
						if dir == 'down':
							y+=1
						elif dir == 'up':
							y-=1
						if dir == 'right':
							x+=1
						elif dir == 'left':
							x-=1
						# print((x, y), 'tuple')

					var = self.Tuple_Decifer(tuple=(x, y))
					# print('<#------------------------------#>')
					listOSC.append('Static')
					if var != None:
						if len(var) == 1:
							listDIR.append(var[0])
						elif len(var) > 1:
							for item in var:
								listDIR.append(item)
					# objMain.My_Collision(OSC='Static', side=var)

				elif obj.get_groupID() in self.__weaponRoster:
					print('weapon')
					listOSC.append('weapon')
					# listDIR.append(var) #define 'var' before uncommenting

				elif obj.get_groupID() in self.__projRoster:
					print('arrow')
					listOSC.append('arrow')
					# listDIR.append(var) #define 'var' before uncommenting

				elif obj.get_groupID() in self.__staticRoster:
					print('static')
					listOSC.append('N\A')
					# listDIR.append(var) #define 'var' before uncommenting
			print('\n\n\n')
			print('<#----------------------------#>')
			print(len(listOSC), ':Items in list')
			# print(listOSC, 'list of other "side collision"')
			print(listDIR, 'list of pushing Directions')

			#gets rid of coppy items in list
			# listDIR = self.List_coppyRemover(listDIR)

			#Loops through what is colliding so that no double bounce
			loopTime = 0
			for item in listOSC:
				loopTime += 1
				if len(listOSC) > 1 and len(listDIR) != 0: #multiple entities Colliding
					if loopTime != len(listOSC):
						print(loopTime, len(listOSC), 'loopTime,lenlistOSC')
						if item == listOSC[loopTime]:
							objMain.My_Collision(OSC=item, side=listDIR[loopTime])
						elif item != listOSC[loopTime]:
							objMain.My_Collision(OSC=item, side=listDIR[loopTime])
							objMain.My_Collision(OSC=item, side=listDIR[loopTime-1])
							pass
				else: #when it is only one on one collision
					if len(listDIR) > 0:
						objMain.My_Collision(OSC=item, side=listDIR[0])


		else:
			objMain.My_Collision()
			return


	"""#|----------Extra Functions----------|#"""
	def Tuple_Decifer(self, tuple):
		x, y = tuple
		print(tuple, 'coords')
		result_list = []
		return_list	= []
		if x > 0:
			# print('x > 0, right')
			result_list.append('right')
		elif x < 0:
			# print('x < 0, left')
			result_list.append('left')
		else:
			# print('x = 0, neutral')
			result_list.append('neutral')

		if y > 0:
			# print('y > 0, down')
			result_list.append('down')
		elif y < 0:
			# print('y < 0, up')
			result_list.append('up')
		else:
			# print('y = 0, neutral')
			result_list.append('neutral')
		# print('\n')
		# print('<#------------------------------#>')
		# print(result, 'result')
		if result_list[0] != 'neutral' and result_list[1] == 'neutral':
			# print(result[0], 'item 0')
			return_list.append(result_list[0])
			return return_list
		elif result_list[0] == 'neutral' and result_list[1] != 'neutral':
			# print(result[1], 'item 1')
			return_list.append(result_list[1])
			return return_list
		elif result_list[0] != 'neutral' and result_list[1] != 'neutral':
			# print('neither neutral')
			return_list.append(result_list[0])
			return_list.append(result_list[1])
			return return_list

	def List_coppyRemover(self, list):
		lastItem = []
		newList = []
		for item in list:
			if lastItem == []:
				lastItem.append(item)
				newList.append(item)
			elif lastItem != []:
				if item not in lastItem:
					lastItem.append(item)
					newList.append(item)
		return newList




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
