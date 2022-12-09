import turtle

tl = turtle.Turtle()
scr = turtle.Screen()

scr.bgcolor('#262626')
tl.pencolor('#D58BDD')
tl.speed(10)

col = ('#905E96', '#D58BDD', '#FF99D7', '#FFD372')

for n in range(10):
    for x in range(8):
        tl.speed(x+1000)
        for i in range(2):
            tl.pensize(2)
            tl.circle(80+n*7, 90)
            tl.lt(90.2)
        tl.lt(45)
    tl.pencolor(col[n%4])
scr.exitonclick()
turtle.done()