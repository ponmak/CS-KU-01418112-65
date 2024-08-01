# 03 Count Positive Odd Number
counter = 0
while True:
    num = int(input('Enter number: '))
    if num >= 0 and num % 2 != 0:
        counter += 1
    elif num < 0:
        break

print(f'Received {counter} odd numbers')
