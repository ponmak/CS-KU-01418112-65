# 01 Is x an Integer?

num = float(input("Enter a number: "))

if -1 < num < 1:
    print(f'{num} is not an integer.')
else:
    print(f'{num:.0f} is an integer.')
