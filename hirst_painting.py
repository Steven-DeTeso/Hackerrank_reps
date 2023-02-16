# import colorgram

# Extract 6 colors from an image.
# colors = colorgram.extract('hirst_image.jpg', 10)

# print(colors)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as t
import random

t.colormode(255)


tim = t.Turtle()
tim.shape("turtle")
tim.color("green")
tim.speed(0)
tim.penup()
tim.hideturtle()

hirst_painting_colors = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157)]

# Goal: use turtle to paint a 10 x 10 painting with the list above
# Each dot should be about 20 in size and spaced apart by 50 paces

tim.setpos(-275, -200)


num_of_dots = 100

for dot_count in range(1, num_of_dots +1):
    tim.dot(20, random.choice(hirst_painting_colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)










screen = t.Screen()
screen.exitonclick()
