import turtle
import random


turtle.register_shape('bag.gif')
bag_tr = turtle.Turtle()
bag_tr.shape("bag.gif")
bag_tr.penup()

water_tr = turtle.Turtle()
wn = turtle.Screen()
wn.addshape('water.gif')
water_tr.shape('water.gif')
water_tr.penup()

turtle.register_shape('soda.gif')
soda_tr = turtle.Turtle()
wn = turtle.Screen()
turtle.screensize(420,800)
soda_tr.shape('soda.gif')
wn.addshape('back.gif')
soda_tr.penup()
soda_tr.setposition(-150, -95)

bag_tr.penup()
bag_tr.setposition(450, -85)
water_tr.penup()
water_tr.setposition(150, -95)

good_trash = [bag_tr, water_tr, soda_tr]
hamburger_tr = turtle.Turtle()
wn.addshape('hamburger.gif')
hamburger_tr.shape('hamburger.gif')

hotdog_tr = turtle.Turtle()
wn.addshape('hotdog.gif')
hotdog_tr.shape('hotdog.gif')
hamburger_tr.penup()
hamburger_tr.setposition(0,-95)

hotdog_tr.penup()
hotdog_tr.setposition(300,-110)

tr6 = turtle.Turtle()


fries_tr = turtle.Turtle()
wn.addshape('chips.gif')
fries_tr.shape('chips.gif')
fries_tr.penup()
fries_tr.setposition(600,-100)

heart1 = turtle.Turtle()
wn.addshape('heart.gif')
heart1.shape('heart.gif')

heart3 = turtle.Turtle()
wn.addshape('heart.gif')
heart3.shape('heart.gif')

heart2 = turtle.Turtle()
wn.addshape('heart.gif')
heart2.shape('heart.gif')

hearts_list = [heart1, heart2, heart3]

lives = 3
heart1.penup()
heart1.goto(240,150)

heart2.penup()
heart2.goto(210,150)

heart3.penup()
heart3.goto(180,150)

bad_trash = [hamburger_tr, hotdog_tr, fries_tr]
# make ground
GROUND_LEVEL = -118
wn = turtle.Screen()
wn.bgpic('back.gif')
wn.setup(height = 400, width = 600)
ground = turtle.Turtle()
ground.penup()
ground.goto(-274,GROUND_LEVEL)
#ground.pendown()
ground.penup()
ground.goto(300,GROUND_LEVEL)
ground.penup()
# make player
you = turtle.Turtle()
you.penup()
turtle.register_shape('crocodile.gif')
you.shape('crocodile.gif')
you.goto(-230, GROUND_LEVEL + 27)
you.speed(0)
you.dy = 0
you.dx = 0
you.state = 'ready'
gravity = -0.2
def jump():
  if you.state == 'ready':
    you.dy = 5.5
    you.state = 'jumping'
wn.listen()
wn.onkeypress(jump, "space")
def increase_score():
  score += 100
def decrease_score():
  score -= 50
  
while True:
  you.dy += gravity 
  y = you.ycor()
  y += you.dy
  you.sety(y)
  if you.ycor() < GROUND_LEVEL + 27:
    you.sety(-91)
    you.dy = 0
    you.state = "ready"
 # wn.update()
  hearts = 3      
  score = 0
  # score_tr = turtle.Turtle()
  # score_tr.penup()
  # score_tr.goto(-230, 200)
  # score_tr.write(score, font=("Atari", 15, "normal"))
    
    
  if you.xcor ==  bag_tr.xcor or you.ycor == bag_tr.ycor or you.xcor ==  water_tr.xcor or you.ycor == water_tr.ycor or you.xcor ==  soda_tr.xcor or you.ycor == soda_tr.ycor:
    increase_score()
    #wn.update()

  # if you.xcor ==  hamburger_tr.xcor or you.ycor == hamburger_tr.ycor or you.xcor ==  hotdog_tr.xcor or you.ycor == hotdog_tr.ycor or you.xcor ==  fries_tr.xcor or you.ycor == fries_tr.ycor:
  #   wn.update()



  count = 0
  
  smoke = 0
  a = True
  ycors4 = [600,GROUND_LEVEL,600,-20]
  ycors5 = [600,GROUND_LEVEL,600,-20]
  ycors7 = [600,GROUND_LEVEL,600,-20]


  bag_tr.back(3)
  water_tr.back(3)
  soda_tr.back(3)
  hamburger_tr.back(3)
  hotdog_tr.back(3)
  fries_tr.back(3)

#def cloud2():
  
  if hamburger_tr.xcor() <= -330:
    hamburger_tr.goto(random.randint(300,400),GROUND_LEVEL+27)
  elif you.distance(hamburger_tr.pos()) <= 10:
   hearts -=1   
   hearts -=1
#def cloud3():
  elif fries_tr.xcor() <= -330:
    fries_tr.goto(random.randint(300,400),GROUND_LEVEL+27)
  elif you.distance(fries_tr.pos()) <= 10:
    hearts -=1
  elif bag_tr.xcor() <= -330:
    bag_tr.goto(random.randint(300,400),GROUND_LEVEL+27)
  elif water_tr.xcor() <= -330:
    water_tr.goto(random.randint(300,400),GROUND_LEVEL+27)
  elif soda_tr.xcor() <= -330:
    soda_tr.goto(random.randint(300,400),GROUND_LEVEL+27)
  turtle.register_shape('giphy.gif')
  if len(hearts_list) == 0:
    you_lose = turtle.Turtle()
    you_lose.shape('giphy.gif')
    you_lose.stamp()
  hearts_list_counter = 0
  bad_trash_counter = 0

  
  if you.distance(hamburger_tr.pos())  <20:
    hearts_list[0].hideturtle()
    hearts_list.pop(0)
    hamburger_tr.goto(random.randint(300,400),GROUND_LEVEL+27)
  elif you.distance(hotdog_tr.pos())  <20:
    hearts_list[0].hideturtle()
    hearts_list.pop(0)
    hotdog_tr.goto(random.randint(300,400),GROUND_LEVEL+27)
  elif you.distance(fries_tr.pos())  <20:
    hearts_list[0].hideturtle()
    hearts_list.pop(0)
    fries_tr.goto(random.randint(300,400),GROUND_LEVEL+27)
    
        
    #  bad_trash_counter += 1
    # hearts_list_counter += 1
#     hearts_list.remove(heart3)
# wn.mainloop()























  
#  # psuedocode for ilay (and everyone if you want# 
#   make a turtle# 
#     have it constantly moving# 
#     have it respond to keyboard inputs so it can jump# 
#     have it fall back to the ground# 
# make map infinite# 
#  change background every certain score count# 
#   keep track of score# 
#   create the pieces of trash# 
#   randomly generate trash using rand om# 
#   increase score number when you hit a recyclable piece of trash# 
#    decrease score when you hit an unrecyclable piece of trash# 
#    if score reaches 0: end game 

