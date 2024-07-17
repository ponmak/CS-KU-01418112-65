PRICE = float(input('Total Price: '))

stamp_cal = int(PRICE // 50)
n = 0

if PRICE < 50:
    print(f'You got: {n}')
else:
    print(f'You got: {n + stamp_cal}')