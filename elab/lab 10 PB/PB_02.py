# 02 ผลรวมสะสม

def accum_sum(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
        print(sum)

l = []

while True:
    num = int(input("Enter a number (0 to end): "))

    if num == 0:
        break
    elif num < 1000 and num > 0:
        l.append(num)
    else:
        print("Number is out of range.")

print("Original list: ")
print(l)
print("Accumulative Sum:")
accum_sum(l)
