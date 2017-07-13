import monopolyVisualisation
import monopolyData

class Piece(object):
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

def draw(board, *pieces):
	monopolyVisualisation.draw(board, pieces)

if __name__ == "__main__":
	import time
	board = Board()
	piece = Piece()

	for i in range(10):
		draw(board, piece)
		time.sleep(1)
		piece.move(1)