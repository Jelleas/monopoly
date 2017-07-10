import monopolyVisualisation
import monopolyData

class Pawn(object):
	def __init__(self, cell):
		self.placeAt(cell)

	def placeAt(self, cell):
		self.cell = cell

class Board(object):
	def __init__(self):
		self.cells = [Cell(name, value) for name, value in zip(monopolyData.names, monopolyData.values)]
		self._pawnLocation = 0
		self.pawn = Pawn(self.cells[self._pawnLocation])
		
	def move(self, distance):
		self._pawnLocation = (self._pawnLocation + distance) % len(self.cells)
		self.pawn.placeAt(self.cells[self._pawnLocation])

class Cell(object):
	def __init__(self, name, value):
		self.name = name
		self.value = value

def draw(board):
	monopolyVisualisation.draw(board)

if __name__ == "__main__":
	import time
	board = Board()

	for i in range(100):
		draw(board)
		time.sleep(1)
		board.move(1)