from models import create_window, create_logo_img, create_title, create_start_button
import button_script


def button_clicked(x, y):
    xcor_left, xcor_right = -284, 284
    ycor_bottom = start_button.ycor() - 73
    ycor_top = ycor_bottom + 146
    if x >= xcor_left and x <= xcor_right and y <= ycor_top and y >= ycor_bottom:
        return True


def left_click(x, y):
    if button_clicked(x, y):
        button_script.button_action(window, start_button)


def shut_down():
    """On key press Esc"""
    window.bye()


def main():
    global window
    global logo_img
    global title
    global start_button

    window = create_window()

    window.listen()
    window.onkeypress(shut_down, 'Escape')
    window.onclick(left_click)

    logo_img = create_logo_img(window.window_width(), window.window_height())

    title = create_title(logo_img.xcor(), window.window_height())

    start_button = create_start_button(logo_img.ycor())

    window.update()
    window.mainloop()


if __name__ == '__main__':
    main()

