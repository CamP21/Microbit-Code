from microbit import *
import random

def show_random_arrow():
    num = random.randrange(8)
    display.show(Image.ALL_ARROWS[num])
    
def spin_animation(num):
    delay = 50
    index = 0
    loops = 0
    while loops < num:
        loops = loops + 1
        display.show(Image.ALL_ARROWS[index])
        sleep(delay)
        delay = delay + 5
        index = index + 1
        if index == 8:
            index = 0

while True:
    if button_a.is_pressed() or button_b.is_pressed():
        spin_animation(30)
        show_random_arrow()
