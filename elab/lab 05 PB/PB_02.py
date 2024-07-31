# 02 ค่าจอดรถ (ยากขึ้น)
import math

hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))
buyAmt = int(input('Enter shopping amount: '))

all_minutes = (hours * 60) + minutes
round_up_hour = math.ceil(all_minutes / 60)