# 09 Find a, b in which a*b=n and (a+b) is the lowest

NUM = int(input())

b = 1
temp = 0

while b < NUM:
    a = int(NUM / b)
    
    if a*b == NUM and temp == 0:
            temp = a+b
            b += 1
            continue
    elif a * b == NUM and temp != 0:
        if temp < a+b:
            b += 1
            continue
        elif temp > a+b:
            temp = a+b
            b += 1
            continue
        else:
            b += 1
            continue
    else:
        b += 1
        continue

print(temp)






