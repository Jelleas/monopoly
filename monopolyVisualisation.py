import Tkinter
import tkMessageBox
import multiprocessing

class MonopolyVisualisation(object):
	def __init__(self, boardQueue):
		self._boardQueue = boardQueue
		self._updateTime = 100
		self._width = 450
		self._height = 450
		self._padding = 0.042 * self._width

		rowLength = 11
		self._cellWidth = (self._width - 2 * self._padding) / float(rowLength)
		self._cellHeight = (self._height - 2 * self._padding) / float(rowLength)

		bottomRow = zip([self._padding + i * self._cellWidth for i in range(rowLength)], [rowLength * self._cellHeight - self._padding] * rowLength)
		bottomRow.reverse()
		topRow = zip([self._padding + i * self._cellWidth for i in range(rowLength)], [self._padding] * rowLength)
		leftColumn = zip([self._padding] * (rowLength - 2), [self._padding + self._cellHeight * i for i in range(1, rowLength - 1)])
		leftColumn.reverse()
		rightColumn = zip([self._padding + (rowLength - 1) * self._cellWidth] * (rowLength - 2), [self._padding + self._cellHeight * i for i in range(1, rowLength - 1)])
		self._cellPositions = bottomRow + leftColumn + topRow + rightColumn

	def run(self):
		self._tk = Tkinter.Tk()
		self._canvas = Tkinter.Canvas(self._tk, height=self._height, width=self._width)
		self._canvas.pack()
		backgroundImage = Tkinter.PhotoImage(file="monopoly_background.gif")
		self._canvas.create_image(0, 0, image = backgroundImage, anchor = "nw")
		self._canvas.background = backgroundImage
		
		self._tk.after(0, self._update)
		self._tk.mainloop()	

	def _reset(self):
		self._canvas.delete("pawn")

	def _update(self):
		if not self._boardQueue.empty():
			self._reset()
			
			board = self._boardQueue.get()
			
			x0, y0 = self._cellPositions[board._pawnLocation]
			carImage = Tkinter.PhotoImage(file="car.gif")
			self._canvas.create_image(x0 + 18, y0 + 18, image=carImage, tag="pawn")
			self._canvas.pawn = carImage

		self._tk.after(self._updateTime, self._update)
		
_boardQueue = None
_visualisationProcess = None
def draw(board):
	global _boardQueue
	global _visualisationProcess
	
	# if visualisation has not started, start
	if not _boardQueue or not _visualisationProcess or not _visualisationProcess.is_alive():
		_boardQueue = multiprocessing.Queue()
		_visualisationProcess = multiprocessing.Process(target=_visualize, args=(_boardQueue,), name="monopolyVisualisation")
		_visualisationProcess.start()

	# add board to the "to be drawed" queue
	_boardQueue.put(board)

def _visualize(boardQueue):
	visualisation = MonopolyVisualisation(boardQueue)
	visualisation.run()