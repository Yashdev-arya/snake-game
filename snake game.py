import turtle
import time
import random
delay=0.2
# set score and high score initial value
score = 0
high_score = 0 
#set up the screen 
wn = turtle.Screen()
wn.title ("snake game by yashdev")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0) 
#  turn off screen updates
#snake head
head =turtle.Turtle()
head.speed(0)
head.color("black")
head.shape("circle")
head.penup()
#from above command head moves but don,t draw anything
head.goto(0,0)
head.direction="stop"
#snake food
food =turtle.Turtle()
food.speed(0)
food.color("pink")
food.shape("square")
food.penup()
#from above command food moves but don,t draw anything
food.goto(0,100)




#function to change the direction of head
def go_up():
      head.direction="up"
def go_down():
      head.direction="down"
def go_left():
      head.direction="left"
def go_right():
      head.direction="right"


# function to move the head

def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)
        
    if head.direction == "down":
        
        y=head.ycor()
        head.sety(y-20)
    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)
#keyboard binding
wn.listen()
wn.onkeypress(go_up,"u")
wn.onkeypress(go_down,"d")
wn.onkeypress(go_left,"l")
wn.onkeypress(go_right,"r")
segments=[]
# pen
pen = turtle.Turtle()
pen.speed(0)
pen .shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
# from above no cursor is shown as shown above in case of head and extra segments
pen.goto(0,260)
pen.write("score:0 high Score:0",align = "center",font =("courier",24,"normal"))
    
while True:
    wn.update()
    #repeatedely refresh the screen
    
    time.sleep(delay)
    #check for border collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290 :
         time.sleep(1)
         head.goto(0,0)
         head.direction = "stop"
         #now as we know extra segment is added if snake is out we have to hide them
         for segment in segments:
              segment.goto(1000,1000)
         segments.clear()
         # reset the score
         score=0
         #now again to avoid overwrite
         pen.clear()
         pen.write("score:{} high Score :{}". format(score,high_score),align="center",font=("courier",24,"normal"))

         

         

              #all segments going out of screen 
         # but all segments appear after that also bcz while loop continuously add it in head after eating and continuously update screen 
          # so we use segments.clear() here  


         

    # for eating of food as known food move as cursor move it cover 20 steps in a single step
    if head.distance(food)<20:
         #now move the food to random place
         x=random.randint(-290,290)
         y=random.randint(-290,290)
         #now as screen disdtance from centre is 300 in each side we can move food curesor to anywhere in that area
         food.goto(x,y)
         #that all inside while loop that continuing working 
         #now after eating food a segment is added in snake 
         new_segment =turtle.Turtle()
         new_segment.speed(0)
         new_segment.color("black")
         new_segment.shape("circle")
         new_segment.penup()
         segments.append(new_segment)
         #now a new body is created but this body is sepreated from previous cursor that mean from our actual snake 
         #it must move with head
         #increase the score
         # shorten the delay
         delay-=0.001
         score+=10
         if score>high_score:
              high_score = score
          #to avoid overwrite here cursor write score  over other if score  is increasing so we have to clear previous score first
         pen.clear()
         pen.write("score:{} high Score :{}". format(score,high_score),align="center",font=("courier",24,"normal"))

    #move the end segments first in reverse order
    #in that case each time jo newturtle create hoga wo last mai attach hota zaayega 
    for index in range (len(segments)-1,0,-1):
         #from statement given below it is specify that x and y is coordinate of index before that index where last element present so it is assign to that last one also

         x=segments[index-1].xcor()
         y=segments[index-1].ycor()
         segments[index].goto(x,y)
    #now segment is created and they joined one after other but it is necessary to move all with head segment for this find coordinated of head and give to zero index if any element is present in segment

    if len(segments)>0:
         x=head.xcor()
         y=head.ycor()
         segments[0].goto(x,y)
    move()
    #check for head collision with the body
    for segment in segments :
         if segment.distance(head)<20:
              time.sleep(1)
              head.goto(0,0)
              head.direction="stop"
              # again clear the segments
              for segment in segments:
                   segment.goto(1000,1000)
                   segment.clear()
    
    

wn.mainloop()