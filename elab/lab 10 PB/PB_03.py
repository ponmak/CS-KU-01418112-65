# 03 ค่าความแปรปรวน

import math

def find_sd(l):
    # cal sd
    sigma = 0 # find sigma func fxk math grade 12
    for i in l:
        sigma += (i - (sum(l) / len(l)))**2

    sd = math.sqrt(sigma/ (len(l)-1))

    return sd # return tuple like list but can't del value

scores = []

while True:
    num = float(input("Enter score: "))

    if num == -1:
        break
    elif num <= 100 and num > -1:
        scores.append(num)
    else:
        print("Score is out of range.")

if len(scores) != 0:
    print(f"Maximum score is {max(scores):.2f}.")
    print(f"Minimum score is {min(scores):.2f}.")
    print(f"Average score is {sum(scores) / len(scores):.2f}.")
    print(f"Standard deviation is {find_sd(scores):.2f}.")
