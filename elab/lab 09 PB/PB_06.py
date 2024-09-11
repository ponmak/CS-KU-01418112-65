# 06 Alternating Sum

def Alt_sum(num):
    i = 1
    sum_ = 0
    while i <= num:
        if i % 2 == 0:
            sum_ -= i
        else:
            sum_ += i
        i += 1
    return sum_

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n,Alt_sum(n)))