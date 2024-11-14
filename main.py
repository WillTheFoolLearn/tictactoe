#!/usr/bin/python3
from graphics import Window
from game import TakeTurn
import tkinter as tk


def main():
    win = Window(800, 800)
    TakeTurn(win)
    tk.mainloop()

if __name__ == "__main__":
    main()