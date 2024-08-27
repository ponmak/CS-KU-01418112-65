# Super Easy Triangle

h = int(input())
text = input()

max_text = 26
if text == "upper":
    temp_h = h * 2 - 1
    upper_num = 65

    i = 0
    while i < h:
        j = 0
        triangle_t = ""
        triangle_t += " "*i
        new_j = 0

        while j < temp_h:
            if j < 26:
                triangle_t += chr(upper_num + j)
            else:
                while new_j < max_text:
                    lower_num = 97
                    triangle_t += chr(upper_num + new_j)
                    new_j += 1
            j += 1


        temp_h -= 2
        upper_num +=1
        i += 1
        print(triangle_t)
elif text == "lower":
    temp_h = h * 2 - 1
    lower_num = 97

    i = 0
    while i < h:

        j = 0
        triangle_t = ""
        triangle_t += " "*i
        new_j = 0

        while j < temp_h:
            if j < 26:
                triangle_t += chr(lower_num + j)
            else:
                lower_num = 97
                triangle_t += chr(lower_num + new_j)
                new_j += 1
            j += 1

        temp_h -= 2
        lower_num +=1
        i += 1
        print(triangle_t)

elif h <= 0 or h > 26:
    print("Invalid case.")
else:
    print("Invalid case.")
