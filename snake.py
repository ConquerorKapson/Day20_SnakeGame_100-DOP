from turtle import Turtle, Screen

MOVE_DISTANCE = 22
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.position = 0
        self.kachua_list = []
        self.create_snake()
        self.head = self.kachua_list[0]

    def create_snake(self):
        for i in range(3):
            self.add_body((-MOVE_DISTANCE * i, 0))

    def add_body(self, position):
        kachua = Turtle("circle")
        if position == (0,0):
            kachua.shapesize(stretch_len=1, stretch_wid=1.5)
        kachua.color("white")
        kachua.penup()
        kachua.goto(position)
        self.kachua_list.append(kachua)

    def update_snake(self):
        new_pos = self.kachua_list[-1].position()
        self.add_body(new_pos)

    def move(self):
        for i in range(len(self.kachua_list) - 1, 0, -1):
            new_x = self.kachua_list[i - 1].xcor()
            new_y = self.kachua_list[i - 1].ycor()
            self.kachua_list[i].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def body_collide(self):
        for part in self.kachua_list[1:]:
            if self.head.distance(part) < 10:
                return True

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def reset(self):
        for part in self.kachua_list:
            part.goto(1000, 1000)
        self.position = 0
        self.kachua_list.clear()
        self.create_snake()
        self.head = self.kachua_list[0]
