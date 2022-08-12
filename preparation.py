# import turtle as t
# screen = t.Screen()
# pong = t.Turtle()
# screen.register_shape("rectangular", ((0,0),(50,0),(50,10),(0,10)))
# pong.shape("rectangular")

#
# pong.color("white")
# pong.penup()
# # screen.listen()
# def pong_move(x,y):
#     if(y>280):
#         pong.goto(x=-260,y=280)
#     elif(y<-230):
#         pong.goto(x=-260,y=-230)
#     else:
#         pong.goto(x=-260,y=y)
# screen.onclick(pong_move)
# screen.mainloop()


# import turtle as t
# import time
# ball = t.Turtle()
# screen = t.Screen()
# screen.setup(600,600)
# screen.bgcolor("black")
# ball.shape('circle')
# ball.color("white")
# ball.shapesize(1,1)
# ball.penup()
# game_is_on = True
# def wall_collision():
#     if(ball.xcor() == 200 or ball.xcor()==-200):
#         return True
#     return False
# def bouncing():
#     if ball.heading() == 0:
#         ball.setheading(180)
#     elif ball.heading() == 180:
#         ball.setheading(0)
#     else:
#

# screen.tracer(0)
# while game_is_on:
#     ball.forward(10)
#     screen.update()
#     time.sleep(0.02)
#     if wall_collision() == True:
#         bouncing()
#
#
# screen.mainloop()
