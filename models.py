"""
Objects atributtes displayed on screen setted in this module
"""

import turtle
from tkinter import Image
import os

PATH = os.path.dirname(os.path.abspath(__file__)) + '\\'

# Window Object
def create_window():
    window = turtle.Screen()
    window.title('WhatsApp Statistics')
    favicon = Image("photo", file=(PATH + 'images/favicon.png'))
    turtle._Screen._root.iconphoto(True, favicon)
    window.bgcolor('#040604')
    window.setup(width= 1.0, height= 1.0, startx=0, starty=0)
    window.tracer(0)
    window.addshape(PATH + 'images/logo.gif')
    window.addshape(PATH + 'images/button.gif')
    return window


def create_logo_img(window_width, window_height):
    logo_img = turtle.Turtle()
    logo_img.shape(PATH + 'images/logo.gif')
    logo_img.penup()
    logo_img.setx((window_width // 4.75) * -1)
    logo_img.sety((window_height // 4))
    logo_img.showturtle()
    return logo_img


def create_title(logo_x_coord, window_height):
    title = turtle.Turtle()
    title.color('#f0f0f0')
    title.hideturtle()
    title.penup()
    title.setx(logo_x_coord + 400)
    title.sety((window_height // 4) -30)
    title.write('WhatsApp Statistics', align='center', font=('Calibri', 48, 'bold'))
    return title


def create_start_button(logo_y_coord):
    start_button = turtle.Turtle()
    start_button.penup()
    start_button.shape(PATH + 'images/button.gif')
    start_button.sety(logo_y_coord - 300)
    start_button.color('#f0f0f0')
    return start_button