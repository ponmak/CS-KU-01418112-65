# PB_08.py
day_index = input() 
day_in_months = int(input())

MODUL_DAY = 0

if day_index == 'Sunday':
    day_index = 1
elif day_index == 'Monday':
    day_index = 2
elif day_index == 'Tuesday':
    day_index = 3
elif day_index == 'Wednesday':
    day_index = 4
elif day_index == 'Thursday':
    day_index = 5
elif day_index == 'Friday':
    day_index = 6
elif day_index == 'Saturday':
    day_index  = 7

# Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
if day_index > 7 or day_index < 1 or day_in_months > 32:
    print('ERROR')
else:
    MODUL_DAY = day_in_months % 7 
    print(MODUL_DAY)