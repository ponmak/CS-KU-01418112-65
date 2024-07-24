# 04 ระยะทาง

import math

while True:
    
    print('<<Point a>>')
    ax = int(input('Enter x coordinate: '))
    ay = int(input('Enter y coordinate: '))
    
    print('<<Point b>>')
    bx = int(input('Enter x coordinate: '))
    by = int(input('Enter y coordinate: '))

    if ax == 0 and ay == 0 and bx == 0 and by == 0:
        print('Goodbye')
        break
    
    EUCLIDEAN_DISTANCE = math.sqrt(((ax - bx)**2) + ((ay - by)**2)) 
    
    print(f'Distance between ({ax}, {ay}) and ({bx}, {by}):')
    print(f'Euclidean distance is {EUCLIDEAN_DISTANCE:.2f}.')
    print(f'Horizontal distance is {abs(ax - bx)}.')
    print(f'Vertical distance is {abs(ay - by)}.')

    # north, south, east, west, north-east, north-west, south-east, south-west และ nowhere (เมื่อ a และ b เป็นจุดเดียวกัน)

    if ax == bx and ay == by:
        print('We are going nowhere.')
    elif ax == bx and ay < by:
        print('We are going north.')
    elif ax == bx and ay > by:
        print('We are going south.')
    elif ay == by and ax < bx:
        print('We are going east.')
    elif ay == by and ax > by:
        print('We are going west.')
    elif ay < by and ax < bx:
        print('We are going north-east.')
    elif ay < by and ax > bx:
        print('We are going north-west.')
    elif ay > by and ax < bx:
        print('We are going south-east.')
    else:
        print('We are going south-west.')

