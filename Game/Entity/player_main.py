from .entity_main import Entity_Main
from .player_info import Player_Info
from Weapons import *
from Engine import *

import keyboard

class Player_Main(Entity_Main):
	def __init__(self, cLogic, iNode):
		Entity_Main.__init__(self, info=Player_Info(), cLogic=cLogic, iNode=iNode)
		#----Class Calls----#
		self.__Sword = None
		self.__Bow	 = None
		self.__x	 = 320
		self.__y	 = 320


	#seting up player bellow
	def Player_Setup(self, screenWidth, screenHeight):
		# print(self._kNode, 'Player_SetUP')
		#img setup
		# print(self._iNode, 'Player_SetUP')
		ID = self._info.get_ID()
		imageInfo = self._iNode.Image_Add('z_Pictures/purpuloniousthefirst.png')
		self._info.Image_Data(size=imageInfo[1], pilImage=imageInfo[0], tkImage=imageInfo[2], fileLoc='z_Pictures/purpuloniousthefirst.png')

		#placing the img
		# self.__x, self.__y = self.Random_Place(self._info.get_size(), screenWidth, screenHeight)
		self._iNode.Image_Place(self.__x, self.__y, self._info.get_tkImage(), tag=[ID, self._info.get_groupID()])

		#final set of information save to player
		self._info.Player_Data(coords=(self.__x, self.__y), speed=7, health=10, defense=5, attack=0) #check player_info for well info.
		self._info.set_myCorners(Image_Node.Render.bbox(self._info.get_ID()))

		#Active Parameters
		self._myHealth = self._info.get_health()

	def Movement_Controll(self):
		self._lastDir = []
		if keyboard.is_pressed(self._keyUP):
			self._lastDir.append('up')
			newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), 'up', speed=self._info.get_speed())
			self.Move_Sets(newCoords)
			self._isMoving = True

		if keyboard.is_pressed(self._keyDOWN):
			self._lastDir.append('down')
			newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), 'down', speed=self._info.get_speed())
			self.Move_Sets(newCoords)
			self._isMoving = True

		if keyboard.is_pressed(self._keyLEFT):
			self._lastDir.append('left')
			newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), 'left', speed=self._info.get_speed())
			self.Move_Sets(newCoords)
			self._isMoving = True

		if keyboard.is_pressed(self._keyRIGHT):
			self._lastDir.append('right')
			newCoords = self._kNode.Controlled_Move(self._info.get_myCoords(), self._info.get_ID(), 'right', speed=self._info.get_speed())
			self.Move_Sets(newCoords)
			self._isMoving = True

		if keyboard.is_pressed(self._keyUP) == False and keyboard.is_pressed(self._keyDOWN) == False:
			if keyboard.is_pressed(self._keyRIGHT) == False and keyboard.is_pressed(self._keyLEFT) == False:
				self._isMoving = False

		return self._isMoving

	def Player_MeleeAttack(self):#melee Attack
		if keyboard.is_pressed(self._melee) == True:
			x, y = self._info.get_myCoords() #current coords
			a, b = self.__Sword.get_size()
			if self._lastDir == 'up':
				self.__Sword.Use_Sword(x, y-b, self._lastDir)
			elif self._lastDir == 'down':
				self.__Sword.Use_Sword(x, y+b, self._lastDir)
			elif self._lastDir == 'left':
				self.__Sword.Use_Sword(x-a, y, self._lastDir)
			elif self._lastDir == 'right':
				self.__Sword.Use_Sword(x+a, y, self._lastDir)
			self._isAttack = True
			return self._isAttack

		elif self.__Sword.get_isActive() == False:
			self._isAttack = False
			return self._isAttack

	def Player_RangedAttack(self):#ranged attack
		if keyboard.is_pressed(self._ranged) == True:
			x, y = self._info.get_myCoords() #current coords
			a, b = self.__Bow.get_size()
			if self._lastDir == 'up':
				self.__Bow.Use_Bow(x, (y-b), 'up')
			elif self._lastDir == 'down':
				self.__Bow.Use_Bow(x, (y+b), 'down')
			elif self._lastDir == 'left':
				self.__Bow.Use_Bow((x-a), y, 'left')
			elif self._lastDir == 'right':
				self.__Bow.Use_Bow((x+a), y, 'right')
			self._isAttack = True
			# print(self._isAttack)
			return self._isAttack

		elif self.__Bow.get_isActive() == False:
			self._isAttack = False
			# print(self._isAttack)
			return self._isAttack

	def Player_Attack(self):
		self.Player_MeleeAttack()
		self.Player_RangedAttack()




	"""#|--------------Getters--------------|#"""
		#this is where a list of getters will go...
	def get_weaponOut(self):
		return self._isAttack


	"""#|--------------Setters--------------|#"""
		#this is where a list of setters will go...
	def set_weapons(self, sword, bow):
		self.__Sword = sword
		self.__Bow	 = bow

	def set_ammo(self, ammo):
		self.__Bow.set_ammo(ammo)
