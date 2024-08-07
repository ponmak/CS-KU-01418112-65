# 07 วันของเดือนมกราคม

day_start = int(input()) 
day_index = int(input())

# Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
if day_start < 1 or day_start > 7 or day_index < 1 or day_index > 31:
    print("ERROR")
else:
    len_day  = day_index - day_start 
    len_day %= 7

    if len_day == 0:
        print('Sunday')
    elif len_day == 1:
        print('Monday')
    elif len_day == 2:
        print('Tuesday')
    elif len_day == 3:
        print('Wednesday')
    elif len_day == 4:
        print('Thursday')
    elif len_day == 5:
        print('Friday')
    elif len_day == 6:
        print('Saturday')