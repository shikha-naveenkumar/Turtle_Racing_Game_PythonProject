from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(500, 400)
user_bet = screen.textinput("Make a bet!", "Which turtle will win the race? (Violet, Indigo, Green, Yellow, Orange, Red?)")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
ordi = [-150, -90, -30, 30, 90, 150]
turtles = []

race_is_on = False

for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=ordi[i])
    turtles.append(tim)

if user_bet:
    race_is_on = True

while race_is_on:
    for t in turtles:
        if t.xcor() > 230:
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You've won!! The winner is {winning_color}")
            else:
                print(f"You've lost!! The winner is {winning_color}")
            race_is_on = False
        else:
            t.forward(random.randint(0,10))


screen.exitonclick()