import tkinter as tk
from tkinter import messagebox as mb
from tkinter.font import Font
from graphics import Line, Window
import random

class TakeTurn:
    def __init__(self, window):
        self.__window = window
        self.__board = window.board
        self.font = Font(size=28)
        self.turn = random.choice([True, False])
        self.text_canvas = tk.Canvas(window.text_frame, width=window.width)
        
        if self.turn:
            self.turn_text = self.text_canvas.create_text(window.width / 2, (window.height * .1) / 2, font = self.font, text="It's Xs turn")
            window.root.config(cursor="X_cursor")
            self.text_canvas
            self.text_canvas.pack()
        else:
            self.turn_text = self.text_canvas.create_text(window.width / 2, (window.height * .1) / 2, font = self.font, text="It's Os turn")
            window.root.config(cursor="circle")
            self.text_canvas.pack()
        self.tic()
        
        
    def tic(self):
        for frame in self.__board.frames:
            frame.bind('<Button-1>', self.tac)
            
    def tac(self, event):
        index = self.__board.frames.index(event.widget)
        if self.turn:
            self.__board.draw_x(event.widget)
            self.text_canvas.itemconfig(self.turn_text, text="It's Os turn")
            self.__window.root.config(cursor="circle")
            self.text_canvas.pack()
            self.turn = False
            self.__board.board_state[index] = "x"
        else:
            self.__board.draw_o(event.widget)
            self.text_canvas.itemconfig(self.turn_text, text="It's Xs turn")
            self.__window.root.config(cursor="X_cursor")
            self.text_canvas.pack()
            self.turn = True
            self.__board.board_state[index] = "o"
        self.check_win()
    
    def check_win(self):
        win = False
        canvas = self.__window.canvas
        b_s = self.__window.board.board_state
        pos = self.__window.board.positions
        if b_s[0] == b_s[1] == b_s[2] and b_s[0] != 0:
            Line(pos[0], pos[2]).draw(canvas)
            win = True
        if b_s[3] == b_s[4] == b_s[5] and b_s[3] != 0:
            Line(pos[3], pos[5]).draw(canvas)
            win = True
        if b_s[6] == b_s[7] == b_s[8] and b_s[6] != 0:
            Line(pos[6], pos[8]).draw(canvas)
            win = True
        if b_s[0] == b_s[3] == b_s[6] and b_s[0] != 0:
            Line(pos[0], pos[6]).draw(canvas)
            win = True
        if b_s[1] == b_s[4] == b_s[7] and b_s[1] != 0:
            Line(pos[1], pos[7]).draw(canvas)
            win = True
        if b_s[2] == b_s[5] == b_s[8] and b_s[2] != 0:
            Line(pos[2], pos[8]).draw(canvas)
            win = True
        if b_s[0] == b_s[4] == b_s[8] and b_s[0] != 0:
            Line(pos[0], pos[8]).draw(canvas)
            win = True
        if b_s[2] == b_s[4] == b_s[6] and b_s[2] != 0:
            Line(pos[2], pos[6]).draw(canvas)
            win = True
        if 0 not in b_s:
            res = mb.askyesno(title="Game Over", message="It was a draw. Play again?")
            if res == False:
                self.__window.root.destroy()
            else:
                self.__window.board.frames = []
                self.__window.board.board_state = [0 for _ in range(9)]
                self.__window.board.play_box(self.__window.canvas)
                TakeTurn(self.__window)

        if win == True:
            res = mb.askyesno(title="Game Over", message="Would you like to play again?")
            if res == False:
                self.__window.root.destroy()
            else:
                self.__window.board.frames = []
                self.__window.board.board_state = [0 for _ in range(9)]
                self.__window.board.play_box(self.__window.canvas)
                TakeTurn(self.__window)