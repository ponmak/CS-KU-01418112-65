# 04 Factorial table

num = int(input("Enter a number: "))
if num < 0:
    print("Invalid input, program terminates.")
else:
    i = 0
    result = 1 # init result
    while i <= num:
        text_muitply = ""
        if i == 0 or i == 1:
            text_muitply = "1"
            result = 1
        else:
            j = i
            result *= i # result cal
            while j > 0:
                # format
                if j != 1:
                    text_muitply += f"{j} x "
                else:
                    text_muitply += "1"
                j -= 1
        print(f'{i}! = {text_muitply} = {result}')
        i += 1
