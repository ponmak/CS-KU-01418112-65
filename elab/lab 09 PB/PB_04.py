# 04 n!

def factorial(num):
    i = 1
    fac = 1
    while i <= num:
        fac *=i
        i += 1
    return fac

n = int(input("Enter n: "))
print(f"{n}!", "=", factorial(n))