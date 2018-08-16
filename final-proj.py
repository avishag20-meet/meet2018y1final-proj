import turtle
import random
turtle.tracer(1,0)
turtle.penup()


def start(x,y):
    global run
    run = False

run = True
while run:
    turtle.shape("square")
    turtle.write("Winter",font = ('Arial', 20, 'normal'))
    turtle.onclick(start)
    turtle.bg("background")
turtle.clear()
turtle.ht()

#set up postion of eskimo
eskimo = turtle.clone()
eskimo.shape("square")
eskimo.goto(-200,100)
eskimo.st()
SQUARE_SIZE = 20
SQUARE_SIZE1 = 10
eskimo_score = 0
bear_score = 0
scores = turtle.clone()
scores.penup()
scores.pencolor("purple")
scores.goto(0, -400)
turtle.ht()
line = turtle.clone()


line.penup()
line.goto(-100, 350)
line.pendown()
line.write(str(eskimo_score) , align="center", font = ("arial" , 40 , "normal"))

lol = turtle.clone()
lol.pu()
lol.goto(100,350)
lol.pd()
lol.write(str(bear_score) , align="center", font = ("arial" , 40 , "normal"))


turtle.ht()
#varible list
pos_list = []
stamp_list = []
old_stamp = []
pos_list1 = []
bear_score = 0
eskimo_score = 0
food_pos=[]
food_stamps=[]

#set up position of bear
bear = turtle.clone()
bear.shape("circle")
bear.goto(200,100)
bear.st()
#turtle.register_shape("turtle")

food = turtle.clone()
food.shape("turtle")
food_pos = []
food_stamps = []

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
TIME_STEP = 100

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction1 = UP
W_ARROW = "w"
A_ARROW = "a"
S_ARROW = "s"
D_ARROW = "d"
W = 10
S = 11
A = 12
D = 13
direction2 = S
LEFT_EDGE = -550
RIGHT_EDGE = 550
UP_EDGE = 500
DOWN_EDGE = -500







def up():
    global direction1
    direction1 = UP
    print("you pressed the up key!")
    #move_characters()
    
def down():
    global direction1
    direction1 = DOWN
    print("you pressed the down key!")
    #move_characters()

def left():
    global direction1
    direction1 = LEFT
    print("you pressed the left key!")
    #move_characters()
    
def right():
    global direction1
    direction1 = RIGHT
    print("you pressed the right key!")
    #move_characters()
    
def up1():
    global direction2
    direction2 = W
    print("you pressed the W key!")
    #move_characters()
    
def down1():
    global direction2
    direction2 = S
    print("you pressed the S key!")
    #move_characters()

def left1():
    global direction2
    direction2 = A
    print("you pressed the A key!")
    #move_characters()
    
def right1():
    global direction2
    direction2 = D
    print("you pressed the D key!")
    #move_characters()

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(up1, W_ARROW)
turtle.onkeypress(down1, S_ARROW)
turtle.onkeypress(left1, A_ARROW)
turtle.onkeypress(right1, D_ARROW)
turtle.listen()

def make_food():
    global food
    min_x=int(LEFT_EDGE/SQUARE_SIZE)+1
    max_x=int(RIGHT_EDGE/SQUARE_SIZE)-1
    min_y=int(DOWN_EDGE/SQUARE_SIZE)-1
    max_y=int(UP_EDGE/SQUARE_SIZE)+1
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x, food_y)
    food_pos.append(food.pos())
    food_stmp = food.stamp()
    food_stamps.append(food_stmp)
for i in range (20):
    make_food()
  
def move_characters():
    my_pos = bear.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
   
    
    
    if direction1 == RIGHT:
        if x_pos >= RIGHT_EDGE:
            bear.goto(LEFT_EDGE, y_pos)
        else:
            bear.goto (x_pos + SQUARE_SIZE  ,y_pos)
        print("right")
    elif direction1 == LEFT:
        if x_pos <= LEFT_EDGE:
            bear.goto (RIGHT_EDGE, y_pos)
        else:
            bear.goto (x_pos - SQUARE_SIZE, y_pos)
        print("left")
    elif direction1 == UP:
        if y_pos >= UP_EDGE:
            bear.goto(x_pos, DOWN_EDGE)
        else:
            bear.goto (x_pos, y_pos + SQUARE_SIZE)
        print("up")
    elif direction1 == DOWN:
        if y_pos<=DOWN_EDGE:
            bear.goto(x_pos, UP_EDGE)
        else:
            bear.goto (x_pos, y_pos -SQUARE_SIZE)
        print ("down")
  
    my_pos=bear.pos()
    pos_list.append(my_pos) 

    
    global pos_list1
    my_pos1 = eskimo.pos()
    x_pos1 = my_pos1[0]
    y_pos1 = my_pos1[1]

    if direction2 == D:
        if x_pos1>= RIGHT_EDGE:
            eskimo.goto(LEFT_EDGE, y_pos1)
        else:
            eskimo.goto (x_pos1 + SQUARE_SIZE1  ,y_pos1)
        print("right")
    elif direction2 == A:
        if x_pos1<= LEFT_EDGE:
            eskimo.goto(RIGHT_EDGE, y_pos1)
        else:
            eskimo.goto (x_pos1 - SQUARE_SIZE1, y_pos1)
        print("left")
    elif direction2 == W:
        if y_pos1 >=  UP_EDGE:
            eskimo.goto(x_pos1, DOWN_EDGE)
        else:
            eskimo.goto (x_pos1, y_pos1 + SQUARE_SIZE1)
        print("up")
    elif direction2 == S:
        if y_pos1 <= DOWN_EDGE:
            eskimo.goto(x_pos1, UP_EDGE)
        else:
            eskimo.goto (x_pos1, y_pos1 -SQUARE_SIZE1)
        print ("down")
        
    global food_stamps, food_pos, bear_score, eskimo_score
    if bear.pos() in food_pos:
        food_ind=food_pos.index(bear.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("you have eaten the food!")
        bear_score = bear_score+1
        lol.clear()
        lol.write(str(bear_score) , align="center", font = ("arial" , 40 , "normal"))

        print(bear_score)
                           
    if eskimo.pos() in food_pos:
        food_ind=food_pos.index(eskimo.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("you have eaten the food!")
        eskimo_score = eskimo_score+1
        line.clear()
        line.write(str(eskimo_score) , align="center", font = ("arial" , 40 , "normal"))
        
        print(eskimo_score)
        #scores.pendown()
        #scores.clear()
        #scores.write((score), align = "center", font = ("david", 20, "normal"))
        #global TIME_STEP
        #TIME_STEP = TIME_STEP-1
    if len(food_pos)==10:
        quit()
    my_pos1=eskimo.pos()
    pos_list1.append(my_pos1)
    turtle.ontimer(move_characters, TIME_STEP )
    
move_characters()



x=0

#cnoble@meet.mit.edu

