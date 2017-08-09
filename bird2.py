import turtle
import time
import pygame
import random

turtle.tracer(2,0)

size_x = 800
size_y = 500
turtle.setup(size_x, size_y)
square_size = 20
start_y_pos = 100
TIME_STEP = 100
tube_list = []
counter = 0
counter2 = 0

SIZE_X=1200
SIZE_Y=900
turtle.setup(SIZE_X,SIZE_Y)
turtle.bgcolor("light blue")

def create_tube():
    tube = turtle.clone()
    tube.penup()
    tube.shape('square')
    tube2=turtle.clone()
    tube2.penup()
    tube2.shape('square')
    # getting valid random tube positions
    tube1_y = random.randint(0,size_y/2)
    tube2_y = random.randint(0,size_y/2)
    while abs(tube1_y - tube2_y) < 3 * square_size:
        tube1_y = random.randint(0,size_y/2)
        tube2_y = random.randint(0,size_y/2)
    tube.goto(size_x/2,tube1_y)
    tube2.goto(size_x/2,tube2_y)
    tube_list.append(tube)
    tube_list.append(tube2)
##    turtle.ontimer(create_tube, 1000)

def move_tubes():
    global counter,counter2, tube_list
    for tube in tube_list:
        my_pos = tube.pos()
        x_pos = my_pos[0]
        y_pos = my_pos[1]
        if x_pos < -size_x/2:
            tube_list.remove(tube)
        
        tube.goto(x_pos - square_size,y_pos)

    counter += 1
    if counter%10 == 0:
        create_tube()
##    create_tube()

##    turtle.ontimer(move_tubes,TIME_STEP)


create_tube()
##move_tubes()



pygame.mixer.init()

pygame.mixer.music.load("ibeli.mp3")

pygame.mixer.music.play(-1)

timing = 0
turtle.setup(size_x,size_y)
##turtle.hideturtle()
turtle.register_shape("newnewnew_bird.gif")
turtle.register_shape("poof.gif")

writer = turtle.clone()
writer.hideturtle()
writer.penup()
writer.goto(200, 250)
##writer.write("This way to Kenya -->", font=("Arial", 24, "normal"))
##writer.goto(200, 210)
##writer.write("get there to give the", font=("Arial", 24, "normal"))
##writer.goto(200, 170)
##writer.write("children food!", font=("Arial", 24, "normal"))
##writer.goto(-530, 250)
#writer.write("You'll get to Kenya in: ", font=("Arial", 24, "normal"))

birdy = turtle.clone()
birdy.shape("newnewnew_bird.gif")
birdy.penup()
birdy.showturtle()

score = turtle.clone()
score.penup()
score.hideturtle()
score.goto(-210, 250)

UP_ARROW = "Up"
LEFT_ARROW = "Left"

draw = turtle.clone()
draw.hideturtle()
def times():
    global time
    timing += 1

def grav():
    global timing
    my_pos = birdy.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    birdy.goto(x_pos, (y_pos - 10))
    if birdy.pos()[1] > 410:
        draw.write("GAME OVER! :(", font=("Arial", 30, "normal"),align="center")
        pygame.mixer.init()
        pygame.mixer.music.load("hello_darkness.mp3")
        pygame.mixer.music.play()
        time.sleep(17)
        quit()
    if birdy.pos()[1] < -410:
        draw.write("GAME OVER! :(", font=("Arial", 30, "normal"),align="center")
        pygame.mixer.init()
        pygame.mixer.music.load("hello_darkness.mp3")
        pygame.mixer.music.play()
        time.sleep(17)
        quit()
    timing += 1
    score.clear()
    #score.write(str(10000 - timing), font=("Arial", 24, "normal"))
    if timing == 10000:
        draw.write("You won!", font=("Ariel", 30, "normal"),align="center")
        time.sleep(3)
        quit()
    move_tubes()
    turtle.ontimer(grav, 50)
    
def red():
    turtle.bgcolor("red")
turtle.onkeypress(red, LEFT_ARROW)

grav()

def up():
##    move_tubes()
    for i in range(7):
        my_pos = birdy.pos()
        x_pos = my_pos[0]
        y_pos = my_pos[1]
        birdy.goto(x_pos, y_pos + 10)
    
turtle.onkeypress(up, UP_ARROW)
turtle.listen()

if birdy.pos() in tube_list:
    quit()



##global food_stamp,food_pos
##if birdy.pos() in food_pos:
##    global score
##    food_ind=food_pos.index(birdy.pos())
##    food.clearstamp(food_stamp[food_ind])
##    food_stamp.pop(food_ind)
##    food_pos.pop(food_ind)
##    score+=1
##    scorePen = turtle.clone()
##    scorePen.color("light blue")
##    scorePen.shape("square")
##    scorePen.hideturtle()
##    scorePen.penup()
##    scorePen.goto(230, 192)
##    scorePen.stamp()
##    scorePen.goto(230 + SQUARE_SIZE, 192)
##    scorePen.stamp()
##    scorePen.goto(125,175)
##    scorePen.color("black")
##    scorePen.write("Score: " + str(score), font = ("Ariel", 20, "normal"))
##    print("you have eaten the food and scored one point!!!")
##    scorePen.color("white")
##    scorePen.circle(30)
##    make_food()

