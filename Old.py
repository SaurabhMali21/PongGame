import turtle
P1score=0
P2score=0

window=turtle.Screen()
window.title("2PGame")
window.bgcolor("red")
window.setup(width=800,height=600)
window.tracer(0)

P1=turtle.Turtle()
P1.speed(0)
P1.shape("square")
P1.color("yellow")
P1.shapesize(stretch_wid=5,stretch_len=1)
P1.penup()
P1.goto(350,0)

P2=turtle.Turtle()
P2.speed(0)
P2.shape("square")
P2.color("yellow")
P2.shapesize(stretch_wid=5,stretch_len=1)
P2.penup()
P2.goto(-350,0)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ballxdirection=0.2
ballydirection=0.2

score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("score",align="center",font=('ARVO',24,'normal'))

def PRU():
    y=P1.ycor()
    y=y+90
    P1.sety(y)
def PRD():
    y=P1.ycor()
    y=y-90
    P1.sety(y)

def PLU():
    y=P2.ycor()
    y=y+90
    P2.sety(y)
def PLD():
    y=P2.ycor()
    y=y-90
    P2.sety(y)

window.listen()
window.onkeypress(PRU,'w')
window.onkeypress(PRD,'s')
window.onkeypress(PLU,'Up')
window.onkeypress(PLD,'Down')

while True:
    window.update()
    
    ball.setx(ball.xcor()+ballxdirection)
    ball.setx(ball.xcor()+ballxdirection)

    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection=ballxdirection
        P1score=P1score+1
        score.clear()
        score.write("Player1:{} Player2:{}".format(P1score,P2score),align='center',font=('ARVO',24,'normal'))
        
    if ball.xcor()<-390:
        ball.goto(0,0)
        ballxdirection=ballxdirection
        P1score=P1score+1
        score.clear()
        score.write("Player1:{} Player2:{}".format(P1score,P2score),align='center',font=('ARVO',24,'normal'))

    if (ball.xcor()>340)and(ball.xcor()<350)and(ball.ycor()<P1.ycor()+40 and ball.ycor()>P1.ycor()-40):
        ball.setx(340)
        ballxdirection=ballxdirection*-1

    if (ball.xcor()<-340)and(ball.xcor()>-350)and(ball.ycor()<P2.ycor()+40 and ball.ycor()>P2.ycor()-40):
        ball.setx(-340)
        ballxdirection=ballxdirection*-1
        


    




