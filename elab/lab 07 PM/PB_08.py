# 08 วันของเดือนมกราคม 2

day_start = input() 
day_index = int(input())

# Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
if  0 < day_index < 32:
    if day_start == 'Sunday':
        if (day_index - 1) % 7 == 0:
            print('Sunday')
        elif (day_index - 1) % 7 == 1:
            print('monday')
        elif (day_index - 1) % 7 == 2:
            print('Tuesday')
        elif (day_index - 1) % 7 == 3:
            print('Wednesday')
        elif (day_index - 1) % 7 == 4:
            print('Thursday')
        elif (day_index - 1) % 7 == 5:
            print('Friday')
        elif (day_index - 1) % 7 == 6:
            print('Saturday')
    elif day_start == 'Monday':
        if (day_index - 1) % 7 == 0:
            print('Sunday')
        elif (day_index - 1) % 7 == 1:
            print('monday')
        elif (day_index - 1) % 7 == 2:
            print('Tuesday')
        elif (day_index - 1) % 7 == 3:
            print('Wednesday')
        elif (day_index - 1) % 7 == 4:
            print('Thursday')
        elif (day_index - 1) % 7 == 5:
            print('Friday')
        elif (day_index - 1) % 7 == 6:
            print('Saturday')
    elif day_start == 'Tuesday':
        if (day_index - 1) % 7 == 0:
            print('Sunday')
        elif (day_index - 1) % 7 == 1:
            print('monday')
        elif (day_index - 1) % 7 == 2:
            print('Tuesday')
        elif (day_index - 1) % 7 == 3:
            print('Wednesday')
        elif (day_index - 1) % 7 == 4:
            print('Thursday')
        elif (day_index - 1) % 7 == 5:
            print('Friday')
        elif (day_index - 1) % 7 == 6:
            print('Saturday')
    elif day_start == 'Wednesday':
        if (day_index - 1) % 7 == 0:
            print('monday')
        elif (day_index - 1) % 7 == 1:
            print('Tuesday')
        elif (day_index - 1) % 7 == 2:
            print('Wednesday')
        elif (day_index - 1) % 7 == 3:
            print('Thursday')
        elif (day_index - 1) % 7 == 4:
            print('Friday')
        elif (day_index - 1) % 7 == 5:
            print('Saturday')
        elif (day_index - 1) % 7 == 6:
            print('Sunday')
    elif day_start == 'Thursday':
        if (day_index - 1) % 7 == 0:
           print('Tuesday')
        elif (day_index - 1) % 7 == 1:
            print('Wednesday')
        elif (day_index - 1) % 7 == 2:
            print('Thursday')
        elif (day_index - 1) % 7 == 3:
            print('Friday')
        elif (day_index - 1) % 7 == 4:
            print('Sunday')
        elif (day_index - 1) % 7 == 5:
            print('Saturday')
        elif (day_index - 1) % 7 == 6:
            print('monday')
    elif day_start == 'Friday':
        if (day_index - 1) % 7 == 0:
            print('Sunday')
        elif (day_index - 1) % 7 == 1:
            print('monday')
        elif (day_index - 1) % 7 == 2:
            print('Tuesday')
        elif (day_index - 1) % 7 == 3:
            print('Wednesday')
        elif (day_index - 1) % 7 == 4:
            print('Thursday')
        elif (day_index - 1) % 7 == 5:
            print('Friday')
        elif (day_index - 1) % 7 == 6:
            print('Saturday')
    elif day_start == 'Saturday':
        if (day_index - 1) % 7 == 0:
            print('Sunday')
        elif (day_index - 1) % 7 == 1:
            print('monday')
        elif (day_index - 1) % 7 == 2:
            print('Tuesday')
        elif (day_index - 1) % 7 == 3:
            print('Wednesday')
        elif (day_index - 1) % 7 == 4:
            print('Thursday')
        elif (day_index - 1) % 7 == 5:
            print('Friday')
        elif (day_index - 1) % 7 == 6:
            print('Saturday')
    else:
        print("ERROR")
else:
    print("ERROR")