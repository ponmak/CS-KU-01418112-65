# Exercise 5.2
import math

maxx = -math.inf
minn = math.inf

counter = 1
summ = 0

while True:
    num = input()
    if num == '':
        break
    else:
        num = float(num)
        counter += 1
        summ += num

        if maxx < num:
            maxx = num
        if minn > num:
            minn = num

avg = summ / (counter - 1)
print(f'{maxx:.2f} {minn:.2f}')
print(f'{summ:.2f} {maxx:.2f}')

