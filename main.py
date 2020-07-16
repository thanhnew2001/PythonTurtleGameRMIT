import turtle
import os
import random

window = turtle.Screen()
window.setup(800,600)

window.bgpic("images/rmitbackground.gif")
window.tracer(0)

#os.system("afplay sound.mp3&")

b=turtle.Turtle()
window.register_shape("images/duy.gif")
b.shape("images/duy.gif")
b.penup()
b.goto(-300,100)

bullet = turtle.Turtle()
window.register_shape("images/ball.gif")
bullet.shape("images/ball.gif")
bullet.penup()
bullet.goto(0,-250)
bullet.left(60)

trigger = 0
accelerator = 5
bullet_count = 10
game_over = 0
def fire():
    global trigger, accelerator, bullet_count, game_over
    if game_over==0:
        trigger = 1
        accelerator = 5
        os.system("afplay shotgun.wav&")
    else:
        trigger = 0

    if(bullet.ycor()>=300):
        bullet.sety(-250)
        bullet.setx(0)

    weapon.clear()
    bullet_count = bullet_count - 1
    if bullet_count <= 0:
        game_over = 1
        weapon.write('Game over', align="center", font=('Courier', 30))
    else:
        weapon.write(f'Bullets: {bullet_count}', align="center", font=('Courier', 30))


window.listen()
window.onkey(fire,"space")


pen = turtle.Turtle()
pen.hideturtle()
pen.color("red")
pen.penup()
pen.sety(250)
pen.write("Score: 0", align="center", font=('Courier', 30))

weapon = turtle.Turtle()
weapon.hideturtle()
weapon.color("red")
weapon.penup()
weapon.sety(250)
weapon.setx(-200)
weapon.write("Bullets: 10", align="center", font=('Courier', 30))

y = [210,214,218,220]
score = 0

while True:

    if game_over==0:
        b.setx(b.xcor()+5)
        b.sety(random.choice(y))

    if trigger==1:
        accelerator = accelerator + 0.1
        bullet.forward(accelerator)

    if(b.distance(bullet)<=50):
        os.system("afplay explosion.mp3&")
        b.setx(-500)
        score +=1
        pen.clear()
        pen.write(f'Score: {score}', align="center", font=('Courier', 30))

    if(b.xcor()>=500):
        b.setx(-500)

    window.update()
