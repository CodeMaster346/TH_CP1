#TH 2nd Turtle Race
import turtle
import random
import time
import winsound

def setup():
    print("Make sure to have this screen split so that you can see the turtle window and console at the same time.")
    turtle_color_1 = input("Input the color for the first turtle(no uppercase or spaces): ").lower()
    #makes sure that if the user input something with spaces in it they are removed
    fixed_turtle_color_1 = turtle_color_1.replace(" ", "")
    turtle_color_2 = input("Input the color for the second turtle(no uppercase or spaces): ").lower()
    fixed_turtle_color_2 = turtle_color_2.replace(" ", "")
    turtle_color_3 = input("Input the color for the third turtle(no uppercase or spaces): ").lower()
    fixed_turtle_color_3 = turtle_color_3.replace(" ", "")
    turtle_color_4 = input("Input the color for the fourth turtle(no uppercase or spaces): ").lower()
    fixed_turtle_color_4 = turtle_color_4.replace(" ", "")
    turtle_color_5 = input("Input the color for the fifth turtle(no uppercase or spaces): ").lower()
    fixed_turtle_color_5 = turtle_color_5.replace(" ", "")
    screen = turtle.Screen()
    screen.title("Turtle Race")
    screen.bgcolor("limegreen")
    turtle1 = turtle.Turtle()
    turtle1.shape("turtle")    
    turtle2 = turtle.Turtle()
    turtle2.shape("turtle")
    turtle3 = turtle.Turtle()
    turtle3.shape("turtle")   
    turtle4 = turtle.Turtle()
    turtle4.shape("turtle")
    turtle5 = turtle.Turtle()
    turtle5.shape("turtle")
    turtle1.color(f"{fixed_turtle_color_1}")
    turtle2.color(f"{fixed_turtle_color_2}")
    turtle3.color(f"{fixed_turtle_color_3}")
    turtle4.color(f"{fixed_turtle_color_4}")
    turtle5.color(f"{fixed_turtle_color_5}")
    turtle1.penup()
    turtle1.goto(-300, 200)
    turtle1.pendown()
    turtle2.penup()
    turtle2.goto(-300, 100)
    turtle2.pendown()
    turtle3.penup()
    turtle3.goto(-300, 0)
    turtle3.pendown()
    turtle4.penup()
    turtle4.goto(-300, -100)
    turtle4.pendown()
    turtle5.penup()
    turtle5.goto(-300, -200)
    turtle5.pendown()
    finish_line_turtle = turtle.Turtle()
    finish_line_turtle.hideturtle()
    finish_line_turtle.penup()
    finish_line_turtle.color("black")
    finish_line_turtle.goto(300, 400)
    finish_line_turtle.width(10)
    finish_line_turtle.pendown()
    finish_line_turtle.goto(300, -400)
    

def race(seconds):
    bet = input("Which turtle do you want to place a bet on(input color without spaces or capitals)? ").lower()
    fixed_turtle_bet = bet.replace(" ", "")
    for i in range(seconds, 0, -1):
        countdown_turtle.clear()
        countdown_turtle.write(f"{i}", align="center", font=("Arial", 48, "bold"))
        winsound.Beep(500, 400)
        time.sleep(1)
        countdown_turtle.clear()
    countdown_turtle.write("GO!!!!!!!!", align="center", font=("Arial", 48, "bold"))
    winsound.Beep(1000, 1000)
    time.sleep(1)
    countdown_turtle.clear()

    while True:
        for t in turtle.turtles():
            t.forward(random.randint(1, 10))
            if t.xcor() >= 300:
                if t.color()[0] == "black" or t.color()[0] == "purple":
                    continue
                else:
                    winsound.Beep(800, 800)
                    countdown_turtle.goto(0, 0)
                    countdown_turtle.write(f"{t.color()[0].capitalize()} Turtle Wins!", align="center", font=("Arial", 48, "bold"))
                    if t.color()[0] == fixed_turtle_bet:
                        countdown_turtle.goto(0, -100)
                        countdown_turtle.write("Your Bet Was Right!", align="center", font=("Arial", 36, "bold"))
                    else:
                        countdown_turtle.goto(0, -100)
                        countdown_turtle.write("Your Bet Was Wrong!", align="center", font=("Arial", 36, "bold"))
                    return



setup()
countdown_turtle = turtle.Turtle()
countdown_turtle.hideturtle()
countdown_turtle.penup()
countdown_turtle.goto(0, 100)
countdown_turtle.color("purple")
race(3)
turtle.mainloop()
