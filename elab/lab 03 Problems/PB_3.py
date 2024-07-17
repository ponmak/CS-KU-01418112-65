import math

HOUR = int(input('Enter number of hours: '))
MINUTES = int(input('Enter number of minutes: '))

all_minutes = (HOUR * 60) + MINUTES
round_up_hour = math.ceil(all_minutes / 60)

total = 0

if HOUR < 0 or MINUTES < 0 or MINUTES > 59 or HOUR > 23:
    print('Input Error!')
else:
    if all_minutes <= 15: # free 15 first minutes
        total = 0
        print('No charge, thanks.')
    elif 1 <= round_up_hour < 3 : # 1 to 2 hour
        total = 10
        print(f'Total amount due is {total} Bahts.')
    else: # 3 hour or up
        total = 10 * (round_up_hour - 1)
        print(f'Total amount due is {total} Bahts.')


    
    