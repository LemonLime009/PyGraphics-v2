import os

class Matrix:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.empty = "  "
        self.full = " #"
        self.grid = [[self.empty for _ in range(self.width)] for _ in range(self.height)]

    def update(self):
        for row in self.grid:
            print(''.join(row))
    
    def clear(self, mode):
        if mode == 1:
            os.system("clear")
        elif mode == 2:
            for i in range(self.width):
                for j in range(self.height):
                    self.grid[i][j] = self.empty
            os.system("clear")
            self.update()

    def point(self, x, y):
        self.grid[x][y] = self.full

    def line(self, x1, y1, x2, y2):
        if x1 == x2 and y1 != y2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                self.grid[i][x1] = self.full
        elif y1 == y2 and x1 != x2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                self.grid[y1][i] = self.full

    def rect(self, x, y, length, width):
        for i in range(x, x + length):
            for j in range(y, y + width):
                self.grid[i][j] = self.full

    def circle(self, x, y, radius):
        cx = 0
        cy = radius
        decision = 1 - radius

        while cx <= cy:
            self.grid[cy + y][cx + x] = self.full
            self.grid[cx + y][cy + x] = self.full
            self.grid[-cx + y][cy + x] = self.full
            self.grid[-cy + y][cx + x] = self.full
            self.grid[-cy + y][-cx + x] = self.full
            self.grid[-cx + y][-cy + x] = self.full
            self.grid[cx + y][-cy + x] = self.full
            self.grid[cy + y][-cx + x] = self.full

            cx += 1
            if decision <= 0:
                decision += 2 * cx + 1
            else:
                cy -= 1
                decision += 2 * (cx - cy) + 1