import turtle
import math
import colorsys

screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("black")
screen.title("Cosmic Mandala")
screen.colormode(1.0)

ANIM_BATCH = 12
screen.tracer(ANIM_BATCH, 0)

t = turtle.Turtle()
t.shape("turtle")         
t.shapesize(1.2)
t.color("white")
t.showturtle()
t.speed(0)


def hsv(h, s=0.85, v=1.0):
    return colorsys.hsv_to_rgb(h % 1.0, s, v)


def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def spirograph(R=300, r=79, d=120, step=0.02):
    k = (R - r) / r
    total = 2 * math.pi * r         
    t.width(1)
    a = 0.0
    first = True
    while a <= total:
        x = (R - r) * math.cos(a) + d * math.cos(k * a)
        y = (R - r) * math.sin(a) - d * math.sin(k * a)
        t.pencolor(hsv(a / total * 6, 0.7, 0.9))
        if first:
            move(x, y)
            first = False
        else:
            t.goto(x, y)
        a += step
    t.penup()
    screen.update()


def circle_flower(count=36, radius=150):
    t.width(2)
    for i in range(count):
        t.pencolor(hsv(i / count))
        t.penup()
        t.goto(0, 0)
        t.setheading(i * 360 / count)
        t.pendown()
        t.circle(radius)
    t.penup()
    screen.update()


def star_polygon(n=13, m=5, radius=115):
    pts = []
    for i in range(n):
        ang = math.radians(90 + i * 360 / n)
        pts.append((radius * math.cos(ang), radius * math.sin(ang)))
    t.width(2)
    idx = 0
    move(*pts[0])
    for i in range(n + 1):
        t.pencolor(hsv(i / n + 0.5, 0.3, 1.0))
        t.goto(*pts[idx])
        idx = (idx + m) % n

    for i, (x, y) in enumerate(pts):
        t.penup()
        t.goto(x, y - 5)
        t.pendown()
        t.pencolor("white")
        t.fillcolor(hsv(i / n))
        t.begin_fill()
        t.circle(5)
        t.end_fill()
    t.penup()
    screen.update()


def sunflower(dots=220, scale=5.2):
    golden = math.radians(137.50776)
    for n in range(1, dots + 1):
        rad = scale * math.sqrt(n)
        ang = n * golden
        x, y = rad * math.cos(ang), rad * math.sin(ang)
        t.penup()
        t.goto(x, y - 2.5)
        t.pendown()
        t.pencolor(hsv(n / dots * 0.9 + 0.05, 0.9, 1.0))
        t.fillcolor(hsv(n / dots * 0.9 + 0.05, 0.9, 1.0))
        t.begin_fill()
        t.circle(2.5 + n / dots * 1.5)
        t.end_fill()
    t.penup()
    screen.update()


spirograph()
circle_flower()
star_polygon()
sunflower()

t.hideturtle()
screen.update()
turtle.done()