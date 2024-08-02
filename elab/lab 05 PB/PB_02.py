# 02 ค่าจอดรถ (ยากขึ้น)
import math

hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))
buyAmt = int(input('Enter shopping amount: '))

all_minutes = (hours * 60) + minutes
round_up_hour = math.ceil(all_minutes / 60)

total = 0

if hours < 0 or hours > 20 or minutes < 0 or minutes > 59 or (hours == 20 and minutes > 0):
    print('Invalid time.')
else:
    if 1 <= round_up_hour < 3 or buyAmt > 3000:
        print('No charge, thank you.')
        pass
    elif 3 <= round_up_hour <= 4 and not 300 <= buyAmt <= 3000:
        total = 20 * (round_up_hour - 2)
        print(f'Total amount due is {total} Baht, thank you.')
    elif 3 <= round_up_hour <= 4 and  300 <= buyAmt <= 3000:
        print('No charge, thank you.')
        pass
    elif round_up_hour > 5 and not buyAmt > 3000 and not 300 <= buyAmt <= 3000:
        total = 40 + 50 * (round_up_hour - 4)
        print(f'Total amount due is {total} Baht, thank you.')
    else:
        total = 50 * (round_up_hour - 4)
        print(f'Total amount due is {total} Baht, thank you.')



    
    