# 03 Triangle alphabet 3

num = int(input("Enter a number: "))
str_ = ''

if num > 26 or num <= 0:
    print("Invalid input, program terminates.")
else:
    i = 0
    while i < num-1:
        str_ += chr(ord('A') + i)
        print(str_)
        i += 1

    i = num
    str_ = ""

    while i > 0:
        # inti j loop
        j = 0
        while j < i:
            str_ += chr(ord('A') +j)
            j += 1
        print(str_)
        str_= ""
        i -= 1
