import tkinter as tk

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title('Tic Tac Toe')
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)
        self.__frame = tk.Frame(self.root, bg="white", width=width, height=height)
        self.canvas = tk.Canvas(self.__frame, highlightthickness=0, bg="white", width=width * .9, height=height * .9)
        self.__frame.pack(expand=True)
        self.__frame.pack_propagate(False)
        self.canvas.pack(expand=True)
        self.board = Board(width * .9, height * .9)
        self.win_draw_board(self.board, self.canvas)
        self.text_frame = tk.Frame(self.__frame, width=width, height = height * .05)
        self.text_frame.pack(fill="both", expand=True)
        self.board.play_box(self.canvas)
        self.canvas.tag_raise("above", "grid")
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def win_draw_board(self, board, canvas):
        board.draw_board(canvas)

class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1:Point, p2:Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black", width=10):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=width, tags="above")

class Circle:
    def __init__(self, p1:Point, p2:Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, outline_color="black", width=10):
        canvas.create_oval(self.p1.x, self.p1.y, self.p2.x, self.p2.y, outline=outline_color, width=width, tags="above")

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board_state = [ 0 for _ in range(9)]
        self.positions = [
            Point(self.width * 1/6, self.height * 1/6),
            Point(self.width * 3/6, self.height * 1/6),
            Point(self.width * 5/6, self.height * 1/6),
            Point(self.width * 1/6, self.height * 3/6),
            Point(self.width * 3/6, self.height * 3/6),
            Point(self.width * 5/6, self.height * 3/6),
            Point(self.width * 1/6, self.height * 5/6),
            Point(self.width * 3/6, self.height * 5/6),
            Point(self.width * 5/6, self.height * 5/6)
        ]
        self.frames = []

    def draw_board(self, canvas):
        self.v1 = Line(Point(self.width * (1/3), 0), Point(self.width * (1/3), self.height))
        self.v2 = Line(Point(self.width * (2/3), 0), Point(self.width * (2/3), self.height))
        self.h1 = Line(Point(0, self.height * (1/3)), Point(self.width, self.height * (1/3)))
        self.h2 = Line(Point(0, self.height * (2/3)), Point(self.width, self.height * (2/3)))
        
        self.v1.draw(canvas)
        self.v2.draw(canvas)
        self.h1.draw(canvas)
        self.h2.draw(canvas)

    def draw_x(self, frame):
        frame_canvas = tk.Canvas(frame, highlightthickness=0, bg="white", height=self.height/4, width=self.width/4)
        line_one = Line(Point(5, 5), Point(self.height/4 - 5, self.width/4 - 5))
        line_two = Line(Point(self.height/4 - 5, 5), Point(5, self.height/4 - 5))
        line_two.draw(frame_canvas, width=10)
        line_one.draw(frame_canvas, width=10)
        frame_canvas.pack()

    def draw_o(self, frame):
        frame_canvas = tk.Canvas(frame, highlightthickness=0, bg="white", height=self.height/4, width=self.width/4)
        circle = Circle(Point(5, 5), Point(self.height/4 - 5, self.width/4 - 5))
        circle.draw(frame_canvas, width=10)
        frame_canvas.pack()

    def play_box(self, canvas):
        for i in range(len(self.board_state)):
            if self.board_state[i] == 0:
                self.frames.append(tk.Frame(canvas, bg="white", height=self.height/4, width=self.width/4))
                canvas.create_window(self.positions[i].x, self.positions[i].y, window=self.frames[i], tags="grid")