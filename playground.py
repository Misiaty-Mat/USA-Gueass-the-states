from turtle import Turtle


class StateWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self, state, x, y):
        self.goto(float(x), float(y))
        self.write(state, move=False)
