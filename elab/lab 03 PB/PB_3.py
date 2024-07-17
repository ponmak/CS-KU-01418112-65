import math

HOUR = int(input('Enter number of hours: '))
MINUTES = int(input('Enter number of minutes: '))

all_minutes = (HOUR * 60) + MINUTES
round_up_hour = math.ceil(all_minutes / 60)

total = 0

print_promte = f'Total amount due is {total} Bahts.'

if HOUR < 0 or MINUTES < 0 :    
    print("Input Error!")
elif all_minutes < 15:
    print('No charge, thanks.')
elif all_minutes >= 120 and all_minutes < 180:
    total = round_up_hour * 10
    print(print_promte)
else:
    
    print(print_promte)

    