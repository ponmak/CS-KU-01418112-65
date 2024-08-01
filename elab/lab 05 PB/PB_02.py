# 02 ค่าจอดรถ (ยากขึ้น)
import math

hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))
buyAmt = int(input('Enter shopping amount: '))

all_minutes = (hours * 60) + minutes
round_up_hour = math.ceil(all_minutes / 60)

if hours < 0 or hours > 20 or minutes < 0 or minutes > 59 or (hours == 20 and minutes > 0):
    print('Invalid time.')
else:
    