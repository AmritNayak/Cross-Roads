from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("navy")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() > 280

    def go_to_start(self):
        self.goto(STARTING_POSITION)
