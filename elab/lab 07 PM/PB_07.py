# 07 วันของเดือนมกราคม

day_start = int(input()) 
day_index = int(input())

# Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
'''
if day_index > 7 or day_index < 1:
    print('ERROR')
else:
    i = day_index
    while i < day_in_months:
        if day_index == 8:
            day_index = 1
            i += 1
        elif i == day_in_months:
            break
        else:
            day_index += 1
            i += 1

    if day_index == 1:
        print('Sunday')  
    elif day_index == 2:
        print('Monday')
    elif day_index == 3:
        print('Tuesday')
    elif day_index == 4:
        print('Wednesday')
    elif day_index == 5:
        print('Thursday')
    elif day_index == 6:
        print('Friday')
    elif day_index == 7:
        print('Saturday') '''
if(day_start < 32 or day_index < 32):

    day_index = day_index % 7 + day_start
    print(day_index)

    if day_index == 1:
        print('Sunday')  
    elif day_index == 2:
        print('Monday')
    elif day_index == 3:
        print('Tuesday')
    elif day_index == 4:
        print('Wednesday')
    elif day_index == 5:
        print('Thursday')
    elif day_index == 6:
        print('Friday')
    elif day_index == 7:
        print('Saturday')
else:
    print('ERROR')