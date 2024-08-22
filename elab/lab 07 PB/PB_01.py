# 01 Triangle alphabet 1

num = int(input("Enter a number: "))
str_ = ''

if num > 26 or num <= 0:
    print("Invalid input, program terminates.")
else:
    i = 0
    while i < num:
        str_ += chr(ord('A') + i)
        print(str_)
        i += 1
