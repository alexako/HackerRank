#!/bin/python
# Head ends here
def nextMove(n,c,r,grid):
	bot = Grid(grid, r, c)
	
	return bot.get_next_move()

class Grid(object):
	def __init__(self, grid, x, y):
		self.grid = grid
		self.botx = x
		self.boty = y
		
	def get_princess_coordinates(self):
		for x, row in enumerate(self.grid):
			for y, col in enumerate(row):
				if col == 'p':
					return (x,y)
	
	def get_next_move(self):
		x = self.botx - self.get_princess_coordinates()[0]
		y = self.boty - self.get_princess_coordinates()[1]
		
		if abs(x) > abs(y):
			if x > 0:
				next_move = "UP"
			else:
				next_move = "DOWN"
		else:
			if y > 0:
				next_move = "LEFT"
			else:
				next_move = "RIGHT"	
		
		return next_move

# Tail starts here
n = input()
x,y = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
	grid.append(raw_input())

print nextMove(n,x,y,grid)
