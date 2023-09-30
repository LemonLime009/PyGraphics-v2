class Matrix:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.empty = "  "
        self.full = " #"
        self.grid = [[self.empty for _ in range(self.width)] for _ in range(self.height)]

    def update(self):
        for row in self.grid:
            print(''.join(row))

    def dot(self, x, y):
        self.grid[x][y] = self.full

    def rect(self, x, y, length, width):
        for i in range(x, x + length):
            for j in range(y, y + width):
                self.grid[i][j] = self.full

    def circle(self, x, y, radius):
    	cx = 0  # Initialize cx and cy to 0
    	cy = radius
    	decision = 1 - radius

    	while cx <= cy:
        	# Plot the eight points of the circle
        	self.grid[cy + y][cx + x] = self.full
        	self.grid[cy + x][cx + y] = self.full
        	self.grid[cy - x][cx + y] = self.full
        	self.grid[cy - y][cx + x] = self.full
        	self.grid[cy - y][cx - x] = self.full
        	self.grid[cy - x][cx - y] = self.full
        	self.grid[cy + x][cx - y] = self.full
        	self.grid[cy + y][cx - x] = self.full

        	cx += 1
        	if decision <= 0:
            	decision += 2 * cx + 1
        	else:
            	cy -= 1
            	decision += 2 * (cx - cy) + 1

matrix = Matrix(20, 20)
matrix.circle(10, 10, 5)
matrix.update()
