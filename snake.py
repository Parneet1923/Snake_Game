from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake():
    def __init__(self):
        self.shape = "square"
        self.color = "green"
        self.segments = []
        self.snake_building()
        self.head = self.segments[0]

    def snake_building(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape=self.shape)
        new_segment.color(self.color)
        new_segment.pu()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.fd(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.snake_building()
        self.head = self.segments[0]
