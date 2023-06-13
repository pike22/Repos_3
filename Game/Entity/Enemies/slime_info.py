from Engine.info_node import Info_Node

class Slime_Info(Info_Node):
	def __init__(self, ID):
		Info_Node.__init__(self, ID=ID, groupID='#slime')


	def Slime_Data(self, coords=None, speed=None, health=None, defense=None, attack=None): #add more here as needed.
		self._baseHealth	= health
		self._baseDefense	= defense
		self._baseAttack	= attack
		self._myCoords		= coords
		self._speed 		= speed
