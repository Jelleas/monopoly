import monopolyData

class Piece(object):
	def __init__(self):
		self.location = 0

	def move(self, distance):
		self.location = (self.location + distance) % len(monopolyData.names)

class Board(object):
	def __init__(self):
		self.names = monopolyData.names[:]
		self.values = monopolyData.values[:]
