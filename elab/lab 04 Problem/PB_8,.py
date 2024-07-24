# 08 เทหรือไม่เท

minute = int(input('Minutes before due: '))
temp = float(input('Temperature: '))
Is_rain = input('Is it raining (y/n)? ').lower()

minute_to_day = round(minute / 1440)

if minute_to_day == 0:
    minute_to_day = 1

print(f'>>> {minute_to_day} days before due.')

if minute_to_day < 2:
    print('>>> I will do the assignment.')
elif minute_to_day > 5:
    print('>>> I will not do the assignment.')
else:
    if temp > 40 or (temp > 25 and Is_rain == 'y'):
        print('>>> I will not do the assignment.')
    else:
        print('>>> I will do the assignment.')
    

    
    
