import multiprocessing
import monopolyVisualisation
		
class Monopoly(object):
	def __init__(self):
		self.board = Board()
		self.pawn = Pawn()
		self._pawnLocation = 0
		
		# start visualisation
		self._boardQueue = multiprocessing.Queue()		
		p = multiprocessing.Process(target=monopolyVisualisation.visualize, args=(self._boardQueue,), name="monopolyVisualisation")
		p.start()
	
	def movePawn(self, distance):
		self._pawnLocation = (self.pawnLocation + distance) % len(self.board.cells)
		self.pawn.placeAt(self.board.cells[self._pawnLocation])

	def draw(self):
		self._boardQueue.put(self.board)

class Pawn(object):
	def __init__(self, cell):
		self.location = cell

	def placeAt(self, cell):
		self.location = cell

class Board(object):
	def __init__(self):
		names = ["start",\
		 		 "dorpstraat",\
		 		 "algemeen fonds",\
		 		 "brink",\
		 		 "inkomstenbelasting",\
		 		 "station zuid",\
		 		 "steenstraat",\
		 		 "kans",\
		 		 "ketelstraat",\
		 		 "velperplein",\
		 		 "gevangenis",\
		 		 "barteljorisstraat",\
		 		 "elecriciteitsbedrijf",\
		 		 "zijlweg",\
		 		 "houtstraat",\
		 		 "station west",\
		 		 "neude",\
		 		 "algemeen fonds",\
		 		 "bilstraat",\
		 		 "vreeburg",\
		 		 "vrij parkeren",\
		 		 "a-kerkhof",\
		 		 "kans",\
		 		 "groote markt",\
		 		 "heerestraat",\
		 		 "station noord",\
		 		 "spui",\
		 		 "plein",\
		 		 "waterleiding",\
		 		 "lange poten",\
		 		 "naar de gevangenis",\
		 		 "hofplein",\
		 		 "blaak",\
		 		 "algemeen fonds",\
		 		 "station oost",\
		 		 "kans",\
		 		 "leidschestraat",\
		 		 "extra belasting",\
		 		 "klaverstraat"]
		values = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120,\
				  0, 140, 120, 140, 160, 200, 180, 0, 180, 200,\
				  0, 220, 0, 220, 240, 200, 260, 260, 150, 280,\
				  0, 300, 300, 0, 320, 200, 0, 380, 0, 400]
		self.cells = [Cell(name, value) for name, value in zip(names,values)]

class Cell(object):
	def __init__(self, name, value):
		self.name = name
		self.value = value

if __name__ == "__main__":
	board = Monopoly()
	board.draw()