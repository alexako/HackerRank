#!bin/python

def displayPathtoPrincess(n, grid):
#print all the moves here
# Tail starts here
	f = Grid(n, grid)
	f.get_bot_coordinates()
	f.get_princess_coordinates()
	f.get_path()

	return
	
class Grid(object):
	def __init__(self, n , grid):
		self.n = n
		self.grid = grid
		
	def get_coordinates_of(self, target):
		for x, row in enumerate(self.grid):
			for y, col in enumerate(row):
				if col == target:
					return (x,y)
		
	def get_bot_coordinates(self):
		return self.get_coordinates_of('m')
		
	def get_princess_coordinates(self):
		return self.get_coordinates_of('p')
		
	def print_path(self, path):
		for move in path:
			print move
		return 

	def get_path(self):
		path = []
		x = self.get_bot_coordinates()[0] - self.get_princess_coordinates()[0]
		y = self.get_bot_coordinates()[1] - self.get_princess_coordinates()[1]
		
		if x > 0:
			row_move = "UP"
		else:
			row_move = "DOWN"
			
		if y > 0:
			col_move = "LEFT"
		else:
			col_move = "RIGHT"
		
		for i in range(abs(x)):
			path.append(row_move)
		for i in range(abs(y)):
			path.append(col_move)
		
		return self.print_path(path)
		
print "Enter grid size: "
m = input()

grid = []
for i in xrange(0, m):
	print "Enter grid row %d: " % (int(i)+1)
	grid.append(raw_input().strip())
	
displayPathtoPrincess(m, grid)
