from turtle import Turtle, Screen
from scoreboard import Scoreboard



class Snake:
    def __init__(self, num_of_segments):
        self.num_of_segments = num_of_segments
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for seg in range(self.num_of_segments):
            self.add_segment(seg)

    def move(self, distance_each_time):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(distance_each_time)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def add_segment(self, seg):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(x=-(seg * 20), y=0)
        new_segment.color("white")
        self.segments.append(new_segment)


    def extend(self):
        self.num_of_segments += 1
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(x=self.segments[-1].xcor(), y=self.segments[-1].ycor())
        new_segment.color("white")
        self.segments.append(new_segment)