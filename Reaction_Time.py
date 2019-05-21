from microbit import *
import random

def wait_button():
    # Wait until button_a or button_b was pressed
    while True:
        if button_a.was_pressed() or button_b.was_pressed():
            break

while True:
    # Show countdown
    display.scroll("321")

    # Wait a few, tense moments...
    delay_time = random.randrange(1000, 5000)
    sleep(delay_time)

    # Display an Image!
    display.show(Image.TARGET)

    # Save start time
    start_time = running_time()

    # Wait for a button press
    wait_button()

    # Calculate the reaction time
    reaction_time = running_time() - start_time

    # Display the result, and keep scrolling
    display.scroll(str(reaction_time), loop = True, wait = False)
    
    # Wait for a button press
    wait_button()
