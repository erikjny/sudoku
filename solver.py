import time
from settings import *
from app_class import *

class Solver:
    def __init__(self, surface):
        self.surface = surface
        self.font = pg.font.SysFont("arial", cellSize//2)

    def solve_sudoku(self):
        row, col = self.find_next_empty(puzzle)

        # Puzzle is solved
        if row is None:
            return True

        # Not solved
        # Make a guess
        for guess in range(1, 10):
            if self.isValid(puzzle, guess, row, col):
                puzzle[row][col] = guess
                self.update_cell(guess, row, col)
                if self.solve_sudoku():
                    return True
        puzzle[row][col] = -1
        self.remove_guess(row, col)

    def find_next_empty(self, puzzle):
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == -1:
                    return row, col
        return None, None

    def isValid(self, puzzle, guess, row, col):
        # Check if guess is in row
        row_vals = puzzle[row]
        if guess  in row_vals:
            return False

        # Check if guess is in column
        col_vals = [puzzle[v][col] for v in range(9)]
        if guess in col_vals:
            return False

        # Check if guess is in 3x3 grid
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3

        for i in range(row_start, row_start + 3):
            for y in range(col_start, col_start + 3):
                if puzzle[i][y] == guess:
                    return False
        return True

    # Show new guess on board
    def update_cell(self, guess, row, col):
        text = self.font.render(str(guess), True, BLACK, WHITE)
        text_rect = text.get_rect()
        text_rect.center = ((gridPos[0] + (row+1)*(cellSize)) - cellSize/2, (gridPos[1] + (col+1)*(cellSize))- cellSize/2)
        self.surface.blit(text, text_rect)
        pg.display.update()

    # Remove last guess from board
    def remove_guess(self, row, col):
        pg.draw.rect(self.surface, WHITE, ((row)*(cellSize)+gridPos[0]+2, (col)*cellSize+gridPos[1]+2, cellSize-4, cellSize-4))
        pg.display.update()
