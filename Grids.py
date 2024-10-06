import turtle

class Grid(turtle.Turtle()):
    def __init__(self):
        super().__init__()
        self.shape="square"
        self.penup()
        self.color("green")
        self.speed("fastest")



