# import colorgram
import turtle
from turtle import Turtle, Screen
import random
# rgb_colors = []
# # Extract (10) colors from an image.
# colors = colorgram.extract("image.jpg", 16)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

screen = Screen()
screen.colormode(255)

color_list = [(203, 34, 66), (71, 116, 151), (228, 161, 193), (246, 253, 251), (252, 246, 250), (150, 184, 70), (151, 160, 164), (242, 235, 46), (37, 161, 80), (35, 31, 32), (137, 205, 187), (240, 99, 54), (75, 65, 40), (33, 162, 165), (240, 246, 249)]

pet = Turtle()
pet.hideturtle()
pet.pensize(5)
pet.speed("slow")
pet.penup()


start_x = -200
start_y = -200
pet.goto(start_x, start_y)


for row in range(10):
    for col in range(10):
        pet.forward(50)
        pet.dot(20, random.choice(color_list))

    new_y = start_y + (row +1) * 50
    pet.goto(start_x, new_y)

screen.exitonclick()