import monopolyVisualisation
import monopolyData

class Pawn(object):
	def __init__(self):
		self.location = 0

	def move(self, distance):
		self.location = (self.location + distance) % 40

class Board(object):
	def __init__(self):
		self.names = monopolyData.names
		self.values = monopolyData.values
	
	def valueAt(self, location):
		return self.values[location]

	def nameAt(self, location):
		return self.names[location]

def draw(board, *pawns):
	monopolyVisualisation.draw(board, pawns)

if __name__ == "__main__":
	import time
	board = Board()
	pawn = Pawn()

	for i in range(10):
		draw(board, pawn)
		time.sleep(1)
		pawn.move(1)