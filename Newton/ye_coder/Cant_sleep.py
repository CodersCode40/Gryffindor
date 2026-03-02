'''Bluiding a traffic light with Python's time and itertools modules.
The traffic light will cycle through red, yellow, and green lights with specified durations for each color. The itertools.cycle function is used to create an infinite loop of the traffic light colors and their durations. The time.sleep function is used to pause the program for the specified duration of each light before moving on to the next one.'''

import time 
from itertools import cycle
lights = [
    ('red', 1.3),
    ('yellow', 2.6),
    ('green', 2)
]
colors = cycle(lights)
n = 10
while n != 0 :
    color, duration = next(colors)
    print(color)
    time.sleep(duration)
    n -= 1   

'''I didn`t understand the color, duration = next(colors), Ai gave them to me and I still don`t know how they work, I know that next(colors) gives me the next item in the cycle, but I don`t understand how it gives me the color and duration separately. I think it has something to do with the way the lights list is structured, but I`m not sure.'''
    # c,s = next(colors)
    # print(c)
    # time.sleep(s)