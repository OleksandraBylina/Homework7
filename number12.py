import turtle

class number12:
    def __init__(self):
        self.position = (-5, 250)

    def draw(self):
        turtle.color("#800080")
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.up()
        turtle.setheading(180)
        turtle.forward(15)
        turtle.down()
        turtle.setheading(90)
        turtle.forward(38)
        turtle.setheading(225)
        turtle.forward(38)
        turtle.penup()
        turtle.goto(self.position[0]-15, self.position[1])
        turtle.pendown()
        turtle.setheading(270)
        turtle.forward(38)
        turtle.setheading(0)
        turtle.forward(18)
        turtle.back(38)

        turtle.penup()
        turtle.goto(self.position[0] + 30, self.position[1]-6)
        turtle.pendown()
        turtle.setheading(60)
        turtle.forward(35)
        turtle.setheading(135)
        turtle.forward(18)
        turtle.setheading(180)
        turtle.forward(18)
        turtle.setheading(225)
        turtle.forward(18)
        turtle.penup()
        turtle.goto(self.position[0] + 30, self.position[1]-6)
        turtle.pendown()
        turtle.setheading(240)
        turtle.forward(35)
        turtle.setheading(135)
        turtle.forward(11)
        turtle.setheading(45)
        turtle.forward(11)
        turtle.setheading(330)
        turtle.forward(32)
        turtle.setheading(45)
        turtle.forward(18)


if __name__ == '__main__':
    eleven=number12()
    eleven.draw()
    turtle.mainloop()