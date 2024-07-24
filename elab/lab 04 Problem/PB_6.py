# 06 ปีอธิกสุรทิน (leap year)

year = int(input('Enter year: '))

if year <= 0:
    print('Invalid year.')
else:
    if year % 400 == 0 and year % 100 == 0:
        print(f'{year} is a leap year.')
    elif year % 4 == 0 and year % 100 != 0:
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')
