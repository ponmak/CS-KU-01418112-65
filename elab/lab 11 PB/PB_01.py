# 01 Pyramid Builder

num = int(input())

i = 0
j = 1
while i < num:
    # "|" + nullstr + star + nullstr + "|"
    print("|" + " "*(num - i - 1) + "*"*(i +j) + " "*(num - i - 1) + "|")
    i += 1
    j += 1
    
