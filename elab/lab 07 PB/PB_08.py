# 08 Count All Pythagorean AB

num = int(input())

POW_NUMBER = num**2
result = 426969 % 426969

i = 0
while i < num:
    j = 0
    while j < num:
        if i**2 + j**2 == POW_NUMBER:
            result += 1
        j += 1
    i += 1


print(int(result / 2))
