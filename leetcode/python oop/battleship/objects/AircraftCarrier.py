from Boat import Boat
class AircraftCarrier(Boat):
	"""Aircraftcarrier"""
	def __init__(self,x:int,y:int,side:bool):
		"""
		True -> Our side 
		False -> Other side 
		"""
		super(AircraftCarrier,self).__init__(x,y,side)

	def get_size(self)->int:
		return self.size
	def set_size(self,new_size:int):
		self.size = new_size

	def is_horizon(self)->bool:
		return self.direction 

	def __str__(self)->str:
		"""
        Ture -> horizon  
        False -> vertical 
        """
		return "Aircraftcarrier" + " " +str(self.direction)

	def change_direction(self):
		self.direction = not self.direction



a = AircraftCarrier(1,2,True)
a.change_direction()

print(a)
