import turtle
import math
import colorsys

TURTLE_SPEED = 8

screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("black")
screen.title("Cosmic Mandala")
screen.colormode(1.0)
screen.tracer(1)               # animate every move

t = turtle.Turtle()
t.shape("turtle")
t.shapesize(1.3)
t.speed(TURTLE_SPEED)


def hsv(h, s=0.85, v=1.0):
    return colorsys.hsv_to_rgb(h % 1.0, s, v)


def go_to(x, y, heading=0):
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()


def star_web(length=400, turn=170, steps=36):
    t.width(1)
    go_to(-length / 2, -length / 3, 0)
    for i in range(steps):
        t.pencolor(hsv(i / steps))
        t.fillcolor(hsv(i / steps))
        t.forward(length)
        t.left(turn)


def circle_flower(count=36, radius=150):
    t.width(2)
    go_to(0, 0, 0)
    for i in range(count):
        t.pencolor(hsv(i / count + 0.5))
        t.fillcolor(hsv(i / count + 0.5))
        t.circle(radius)
        t.left(360 / count)


def star_polygon(n=13, m=5, radius=115):
    turn = m * 360 / n
    edge = 2 * radius * math.sin(math.pi * m / n)
    t.width(3)
    go_to(0, radius, 90 + turn / 2 + 90)
    for i in range(n):
        t.pencolor(hsv(i / n + 0.15, 0.3, 1.0))
        t.fillcolor(hsv(i / n + 0.15, 0.3, 1.0))
        t.forward(edge)
        t.left(turn)


def sunflower(dots=200, scale=5.2):
    golden = math.radians(137.50776)
    for n in range(1, dots + 1):
        r = scale * math.sqrt(n)
        a = n * golden
        c = hsv(n / dots * 0.9 + 0.05, 0.9, 1.0)
        t.penup()
        t.goto(r * math.cos(a), r * math.sin(a) - 3)
        t.setheading(0)
        t.pendown()
        t.pencolor(c)
        t.fillcolor(c)
        t.begin_fill()
        t.circle(2.5 + n / dots * 1.5)
        t.end_fill()


star_web()
circle_flower()
star_polygon()
sunflower()

t.penup()
t.goto(0, 0)
t.hideturtle()
turtle.done()