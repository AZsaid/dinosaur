import turtle
import random
turtle.register_shape('bag.gif')
tr1 = turtle.Turtle()
tr1.shape("bag.gif")
tr2 = turtle.Turtle()
wn = turtle.Screen()

wn.addshape('water.gif')
tr2.shape('water.gif')

turtle.register_shape('soda.gif')
tr3 = turtle.Turtle()
wn = turtle.Screen()
tr3.shape('soda.gif')
wn.addshape('back.gif')
tr3.penup()
tr3.setposition(50, -95)
tr1.penup()
tr1.setposition(150, -85)
tr2.penup()
tr2.setposition(-50, -95)

# make ground
GROUND_LEVEL = -118
wn = turtle.Screen()
wn.bgpic('back.gif')
wn.setup(height = 420, width = 600)
ground = turtle.Turtle()
ground.penup()
ground.goto(-274,GROUND_LEVEL)
ground.pendown()
ground.goto(300,GROUND_LEVEL)
ground.penup()
# make player
you = turtle.Turtle()
turtle.register_shape('ezgif.com-gif-maker (2).gif')
you.shape('ezgif.com-gif-maker (2).gif')
you.penup()
you.goto(-230, GROUND_LEVEL + 27)
you.speed(0)
you.dy = 0
you.dx = 0
you.state = 'ready'
gravity = -0.2
def jump():
  if you.state == 'ready':
    you.dy = 5
    you.state = 'jumping'
wn.listen()
wn.onkeypress(jump, "space")
while True:
  you.dy += gravity
  y = you.ycor()
  y += you.dy
  you.sety(y)
  if you.ycor() < GROUND_LEVEL + 27:
    you.sety(-118 + 27)
    you.dy = 0
    you.state = "ready"
  wn.update()# psuedocode for ilay (and everyone if you want# 
#   make a turt# 
#     have it constantly movi# 
#     have it respond to keyboard inputs so it can ju# 
#     have it fall back to the grou# 
# make map infini# 
#  change background every certain score cou# 
#   keep track of sco# 
#   create the pieces of trash# 
#   randomly generate trash using rand# 
#   increase score number when you hit a recyclable piece of tra# 
#    decrease score when you hit an unrecyclable piece of tra# 
#    if score reaches 0: end game 

 #water_bottle = "recyclabl
# glass_jar = "recycleabl 
# magazine =
# hearts =
# if turtle.distance(water_bottle.pos()) <1
#   hearts = hearts - 
# print(heart
#wn = turtle.Screen()
#wn.addshape("newspaper_100x63(4).gif")







# if True:
#   wn.pos("water_63x63.gif") -= 1
 
#water_bottle = "recyclabl
# glass_jar = "recycleabl 
# magazine =
# hearts =
# if turtle.distance(water_bottle.pos()) <1
#   hearts = hearts - 
# print(heart
#wn = turtle.Screen()
#wn.addshape("newspaper_100x63(4).gif")





#   lives = ['heart1', "heart2", "heart3"]


# while True:
#   my_tr = random.choice(tr1, tr2, tr3)
#   x = my_tr.xcor()
#   x = x - 100
