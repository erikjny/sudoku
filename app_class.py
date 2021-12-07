import pygame as pg
from  button import *
import sys
from settings import *
from solver import Solver

# EN KOMMENTAR
# EN KOMMENTAR Til
class App:
    def __init__(self):
        pg.init()
        self.running = True
        self.mousePos = (0,0)
        self.selected = (0,0)
        self.grid = testBoard
        self.font = pg.font.SysFont("arial", cellSize//2)
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.solve_btn = Button(self.window, 20, 20, 'SOLVE')
        self.reset_btn = Button(self.window, WIDTH-170, 20, 'RESET')
        self.solver = Solver(self.window)

    def run(self):
        self.window.fill(WHITE)
        while self.running:
            self.events()
            self.draw()
            self.update()
        pg.quit()
        sys.exit()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                selected = self.mouseOnGrid()
                if selected:
                    self.selected = selected
                else:
                    self.selected = None
                    print("Not on board")
            # KEY IS PRESSED
            elif event.type == pg.KEYDOWN:
                try:
                    if int(event.unicode) != 0:
                        puzzle[self.selected[0]][self.selected[1]] = int(event.unicode)
                except:
                    pass
                # BACKSPACE PRESSED
                if event.key == pg.K_BACKSPACE:
                    puzzle[self.selected[0]][self.selected[1]] = -1
                # ARROW KEYS TO MOVE ON THE BOARD
                elif event.key == pg.K_UP:
                    new_list = list(self.selected)
                    new_list[1] = (new_list[1]-1)%9
                    self.selected = new_list
                elif event.key == pg.K_DOWN:
                    new_list = list(self.selected)
                    new_list[1] = (new_list[1]+1)%9
                    self.selected = new_list
                elif event.key == pg.K_LEFT:
                    new_list = list(self.selected)
                    new_list[0] = (new_list[0]-1)%9
                    self.selected = new_list
                elif event.key == pg.K_RIGHT:
                    new_list = list(self.selected)
                    new_list[0] = (new_list[0]+1)%9
                    self.selected = new_list

    def draw(self):
        if self.selected:
            self.window.fill(WHITE)
            self.drawSelection(self.window, self.selected)
        if self.solve_btn.draw():
            self.drawNumbers(self.window)
            self.drawGrid(self.window)

            if self.solver.solveSudoku():
                return True;
        if self.reset_btn.draw():
            for i in range(9):
                for y in range(9):
                    puzzle[i][y] = -1
        self.drawGrid(self.window)
        self.drawNumbers(self.window)
        pg.display.update()

    def drawGrid(self, window):
        pg.draw.rect(window, BLACK, (gridPos[0], gridPos[1], WIDTH -150, HEIGHT -150), 2)
        for x in range(9):
            pg.draw.line(window, BLACK, (gridPos[0], gridPos[1]+(x*cellSize)), (gridPos[0]+450, gridPos[1]+(x*cellSize)), 2 if x % 3 == 0 else 1)
            pg.draw.line(window, BLACK, (gridPos[0]+(x*cellSize), gridPos[1]), (gridPos[0]+(x*cellSize), gridPos[1]+450), 2 if x % 3 == 0 else 1)

    ## HELPER METHODS
    def update(self):
        self.mousePos = pg.mouse.get_pos()

    def drawSelection(self, window, pos):
        pg.draw.rect(window, LIGHTBLUE, (pos[0]*cellSize+gridPos[0], pos[1]*cellSize+gridPos[1], cellSize, cellSize))

    def mouseOnGrid(self):
        if self.mousePos[0] < gridPos[0] or self.mousePos[1] < gridPos[1]:
            return False
        elif self.mousePos[0] > gridPos[0] + gridSize or self.mousePos[1] > gridPos[1] + gridSize:
            return False
        return ((self.mousePos[0] - gridPos[0])//cellSize, (self.mousePos[1] - gridPos[1])//cellSize)

    def drawNumbers(self, window):
        for i in range(1, 10):
            for y in range(1, 10):
                tall = puzzle[i-1][y-1]
                if tall > 0:
                    text = self.font.render(str(tall), True, BLACK)
                    text_rect = text.get_rect()
                    text_rect.center = ((gridPos[0] + i*(cellSize)) - cellSize/2, (gridPos[1] + y*(cellSize))- cellSize/2)
                    window.blit(text, text_rect)
