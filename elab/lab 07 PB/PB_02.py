# 02 Triangle alphabet 2

num = int(input("Enter a number: "))

if num > 26 or num <= 0:
    print("Invalid input, program terminates.")
else:
    #inti
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
