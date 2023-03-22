import turtle
turtle.register_shape('bag (copy).gif')

# make ground
GROUND_LEVEL = -118
wn = turtle.Screen()
wn.bgpic('back (copy).gif')
wn.setup(height = 420, width = 600)
ground = turtle.Turtle()
ground.penup()
ground.goto(-274,GROUND_LEVEL)
ground.pendown()
ground.goto(300,GROUND_LEVEL)
ground.penup()
# make player
you = turtle.Turtle()
turtle.register_shape('ezgif.com-gif-maker (6).gif')
you.shape('ezgif.com-gif-maker (6).gif')
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





