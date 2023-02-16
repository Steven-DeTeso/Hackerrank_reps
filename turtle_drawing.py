import turtle as t
import random

t.colormode(255)


tim = t.Turtle()
tim.shape("turtle")
tim.color("chartreuse")
tim.pensize(width=2)
tim.speed(0)

# for _ in range(4):
#     tim.forward(200)
#     tim.right(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

colors = ["red", "orange", "black", "green", "blue", "purple"]

distance = random.randint(20, 50)

directions = [0, 90, 180, 270]

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.circle(100)
        tim.color(random.choice(colors))
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

# def random_walk():
#     tim.forward(distance)
#     tim.speed(0)
#     return tim.setheading(random.choice(directions))

# for _ in range(100):
#     tim.color(random.choice(colors))
#     random_walk()


# def draw_shape(num_sides):
#     """Takes sides of shape as input, figures out angle of shape and uses that to draw"""
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
    

# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)



screen = t.Screen()
screen.exitonclick()
