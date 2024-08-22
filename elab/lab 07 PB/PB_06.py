# 06 Double rectangle stars

higth = int(input("Enter height: "))
width = int(input("Enter width: "))

if higth <= 0 or width <= 0:
    print("Invalid input, program terminates.")
else:
    i = 1
    while i <= higth:
        j = 0
        if i %  2 == 0:
            while j < width:
                print(' *',end='')
                j += 1
        else:
            while j < width:
                print('* ',end='')
                j += 1
        print()
        i += 1
