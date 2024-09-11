# 03 ค่าความแปรปรวน

import math

# กูยำรวมมิตรเลยละกัน
def find_sd(l):
    # sort max
    max_s = 0
    for item in l:
        if max_s < item:
            max_s = item

    # sort min
    min_s = 100
    for item in l:
        if  min_s > item:
            min_s = item

    # cal avg
    avg = sum(l) / len(l)

    # cal sd
    sigma = 0 # find sigma func fxk math grade 12
    for i in l:
        sigma += (i - avg)**2

    sd =math.sqrt(sigma/ (len(l)-1))

    return max_s,min_s,avg,sd # return tuple like list but can't del value

scores = []

while True:
    num = float(input("Enter score: "))

    if num == -1:
        break
    elif num <= 100 and num > -1:
        scores.append(num)
    else:
        print("Score is out of range.")

print(f"Maximum score is {find_sd(scores)[0]:.2f}.")
print(f"Minimum score is {find_sd(scores)[1]:.2f}.")
print(f"Average score is {find_sd(scores)[2]:.2f}.")
print(f"Standard deviation is {find_sd(scores)[3]:.2f}.")
