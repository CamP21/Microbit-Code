from microbit import *
import random
random.seed(2857740885)

wall = Image("55555:00000:00000:00000:00000")
field = Image() 
i_wall = 0
player_x = 2
player_y = 3

score = 0

# Control how often we scroll down
scrollMs = 500
nextScroll = running_time() + scrollMs

# Game Loop
while True:
    # Check for player collision with wall
    if field.get_pixel(player_x, player_y):
        break
    
    # Control player
    if button_a.was_pressed() and player_x > 0:
        player_x = player_x - 1
    if button_b.was_pressed() and player_x < 4:
        player_x = player_x + 1
        
    display.set_pixel(player_x, player_y, 9)
    
    # Is it time to scroll?
    if running_time() > nextScroll:
        # Scroll the field
        field = field.shift_down(1)
        nextScroll = nextScroll + scrollMs
    
        # Update and check wall interval
        i_wall = i_wall + 1
        if i_wall == 3:
            i_wall = 0
            field = field + wall
            
            # Punch hole for gate
            gate = random.randrange(5)
            field.set_pixel(gate, 0, 0)
            
            # Score a point each gate
            score = score + 1
            
            # Increase scroll speed
            if scrollMs > 200:
                scrollMs = scrollMs - 5

        display.show(field)

# Game Over
display.show(Image.SAD)
sleep(500)
display.scroll(str(score), loop=True, wait=False)
