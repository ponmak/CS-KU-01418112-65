# 07 ตัวประกอบที่เป็นจำนวนเฉพาะทั้งหมดของเลขจำนวนเต็ม

def primeNumber(num:int):
    i = 0
    count = 0
    while i < num:
        if num % (i+1) == 0:
            count += 1
        i+=1
    if count == 2:
        return num
    else:
        return None


num = int(input("Enter positive integer: "))

if num <= 0 :
    print("Invalid number.")
else:
        if num == 1:
            pass
        elif primeNumber(num) == num:
            print(num)
        else:

            i = 2
            while i <= num:

                if num % i == 0 and num != 0 and primeNumber(i) == i:
                    print(i)
                    num /= i

                    if num % i == 0:
                        i = i
                    else:
                        i += 1
                elif num != 0 :
                    i += 1
                else:
                    break


# Leo at lampoon's solution
n = int(input("Enter positive integer: "))
i = 2 
if n <= 0:
    print("Invalid number.")
while n != 1 and i <= n:
    if n % i == 0:
        n /= i
        print(i)
    else:
        i += 1
