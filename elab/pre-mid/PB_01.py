# 01 Reduce Steps
num = int(input("Please input number: "))

count = 0

while True:
    print(num)
    if num % 2 == 0 and num != 0:
        num //= 2
        count += 1
        continue
    elif num % 2 != 0:
        num -= 1
        count += 1
        continue
    elif num == 0:
        break

if count == 1:
    step = "step"
else:
    step = "steps"

print(f"{count} {step}")
