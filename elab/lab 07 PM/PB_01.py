# 01 Is x an Integer?

num = float(input())

if  num != int(num):
    print(f'{num} is not an integer.')
else:
    print(f'{num:.0f} is an integer.')
