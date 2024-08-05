# 05 ตึกระฟ้าที่มองเห็น

counter = 0
perv_num = 0 

while True:
    num = int(input())
    if num == -1:
        break
    else:
        if perv_num > num:
            pass
        elif perv_num < num:
            perv_num = num
            counter += 1

print(counter)
