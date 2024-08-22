# 05 ใช่จำนวนเฉพาะไหม?

while True:
    num = int(input("Enter a number: "))

    #con if
    if num == 0:
        print("End of program, goodbye.")
        break
    elif num == 1 or num < 0:
        print("Invalid input, try again.")
        continue
    else:
        i = 0
        count = 0
        while i < num:
            if num % (i+1) == 0:
                count += 1
            i+=1

        if count == 2:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")

        continue
