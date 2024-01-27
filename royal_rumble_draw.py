#script to draw numbers from a hat for the Royal Rumble
#to run: python royal_rumble_draw.py <list of entrants>
import numpy as np
import sys
def draw_nums_from_hat(entrants, num_wrestlers):
    #draw numbers from a hat with no replacement
    #initialize the hat with numbers from 1 to the number of wrestlers
    hat = np.arange(1, num_wrestlers+1)
    #shuffle the hat
    np.random.shuffle(hat)
    #calc the floor of the number of wrestlers divided by the number of entrants
    floor = num_wrestlers//len(entrants)
    #loop through the entrants
    for e in entrants:
        #draw floor numbers from the hat
        draw = hat[:floor]
        #remove the numbers from the hat
        hat = np.delete(hat, np.arange(floor))
        #print the draw
        print(e, draw)
    #print the remaining numbers in the hat
    print('Wild cards', hat)

#take the list of entrants from the command line
entrants = sys.argv[1:]
#30 wrestlers in the Royal Rumble
num_wrestlers = 30
#call the function
draw_nums_from_hat(entrants, num_wrestlers)

