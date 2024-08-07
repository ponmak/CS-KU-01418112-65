# 03 สวัสดีวันจันทร์

day = int(input())
hour = int(input())
minute = int(input())

day_text = ''
time = ''

# Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
if day == 1:
    day_text = 'sunday'
elif day == 2:
    day_text = 'monday'
elif day == 3:
    day_text = 'tuesday'
elif day == 4:
    day_text = 'wednesday'
elif day == 5:
    day_text = 'thursday'
elif day == 6:
    day_text = 'friday'
elif day == 7:
    day_text = 'saturday'

if (hour > 4 and hour < 12) or (hour == 12 and minute < 1) or (hour == 4 and minute >= 1):
    time = 'morning'
elif (hour > 11 and hour < 18) or (hour == 18 and minute <1) or (hour == 12 and minute == 1):
    time = 'afternoon'
elif (hour > 17 and hour < 22) or (hour == 22 and minute < 1) or (hour == 18 and minute == 1):
    time = 'evening'
elif (hour > 21 and hour < 25) or (hour >= 0 and hour < 4) or (hour == 4 and minute < 1):
    time = 'night' 

print(f'good-{time}-{day_text}.png')
