from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
from sudoku import validator, solve_sudoku
import time

class sudokuGUI(Frame):
    
    def __init__(self, parent, game):
        self.game = game
        self.parent = parent
        Frame.__init__(self, parent)

        self.row = 0
        self.column = 0

        self.__initUI()
    
    def __initUI(self):
        self.parent.title("SUDOKU GAME")
        self.pack(fill= BOTH, expand= 1)
        self.canvas = Canvas(self,
                             width=WIDTH,
                             height=HEIGHT)
        