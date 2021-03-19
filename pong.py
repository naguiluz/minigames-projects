import turtle #contains basic programs needed for this projects
import winsound #imports module to do sounds

wn = turtle.Screen() #creates the window that the game will pull up in
wn.title("Pong by @aguiluz_nicolas") #title to appear in window
wn.bgcolor("black") #background color for screen
wn.setup(width=800, height=600) #sets size of our window (+400/-400, +300/-300)
wn.tracer(0) #tracer sets the update time of the window, so zero keeps it from updating

#SCORE scores must be defined first in order to be used in later functions
score_1 = 0
score_2 = 0

# PADDLE A
paddle_a = turtle.Turtle()  #creating and object using the turtle module and the Turtle class from it
paddle_a.speed(0) #speed of animation set to maximum
paddle_a.shape("square") #set shape
paddle_a.color("white") #set color
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #default object size is 20x20pixels. this stretches dimensions by extra pixels so now (100x20)
paddle_a.penup() #turtle objects naturally trace their motion with a line. this turns the line tracing off
paddle_a.goto(-350, 0) #this sets the starting point of our paddle object

# PADDLE B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

#BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .2 #.dx/.dy stands for delta x which means change in coordinates
ball.dy = .2

#DISPLAY
display = turtle.Turtle()
display.speed(0)
display.color("white")
display.penup()
display.hideturtle() #this hides the turtle but not the text
display.goto(0, 260)
display.write("Player 1: 0  Player 2: 0", align="center",font=("Courier", 24, "normal")) #this puts writing in our turtle, aligns it to the center, and sets the style



# PADDLE FUNCTIONS
def paddle_a_up(): #have to create a fucntion for the paddle to move
    y = paddle_a.ycor() #have to set the x/y coordinates, creating a variable to track the y coordinate, .ycor is built into turlte and returns the y coordinate
    y += 50 #add x pixels to the y location
    paddle_a.sety(y) #now setting the y coordinate of paddle_a to y which has been defined as moving up n pixels

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 50
    paddle_a.sety(y)
#if paddle_a.ycor() > 390:
    #paddle_a.goto(390, 0)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 50
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 50
    paddle_b.sety(y)







# KEYBOARD BINDING
wn.listen() #this tells our window to listen for keyboard inputs
wn.onkeypress(paddle_a_up, "w") #now that wn is listening, we set the key press of w to activate our paddle_a_up function
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



# MAIN GAME LOOP
while True:
    wn.update()  #sets the window to update on each loop



    #ball is not controlled by the player, therefore it must do its actions inside the loop, separate from player functions.
    #the balls coordinates are set to this state of constant change as the loops progress
    ball.setx(ball.xcor() + ball.dx)  #setting the location of x as the x coordinate plus the change in x (which was set to n above)
    ball.sety(ball.ycor() + ball.dy)

    #BORDER CHECKING
    if ball.ycor() > 290: #if the ball is over 290 high, then set its coordinates to 290 and set its delta to the opposite direction
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("pongsound.wav", winsound.SND_ASYNC) #this adds in our file using the module and class we imported, windsound.SND_ASYNC makes our sounds asynchronus so it doesnt stop everything to play the sound
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("pongsound.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390: #if the ball is over 390 to either side, reset to center
        ball.goto(0,0)
        ball.dx *= -1
        score_1 += 1
        display.clear() #this clears the previous score
        display.write("Player 1: {}  Player 2: {}".format(score_1,score_2), align="center", font=("Courier", 24, "normal"))  # this sets our score to be updated and formatted as we go
        winsound.PlaySound("pongscore.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_2 += 1
        display.clear()
        display.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("pongscore.wav", winsound.SND_ASYNC)

    #PADDLE AND BALL COLLISION
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50): #if the ball is within the paddle (set at 340-350) and within its dimensions (+/- 50 pixels to account for the paddles size) then reverse its dierection
        ball.setx(340) #essentially setting the ball to edge of the paddle as it reverses direction
        ball.dx *= -1
        winsound.PlaySound("pongsound.wav", winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("pongsound.wav", winsound.SND_ASYNC)