# Night Light w/ ON/OFF
# Needs photocell w/ alligator clips
from microbit import *

# Creates an Empty Image
all_on = Image() # create an empty Image
all_on.fill(9)   # set all pixels to max brightness = 9

pin0.read_digital() # Setup Pin0

while True:
    # Read pin0: returns 0=dark to 1023=bright
    value = pin0.read_analog()
    
    # Convert value to a 0-9 "lamp_level"
    light_level = int(value / 113)
    lamp_level = 9 - light_level
    
    # Set all pixels to lamp_level
    all_on.fill(lamp_level)
    
    if value < 500:
        display.show(all_on)
    else:
        display.clear()
