# 05ตัดเลขที่ไม่เรียงลำดับออกจากลิสต์

num_list = []
max = 0
while True:
    num = int(input())

    if num == -1:
        break
    elif  max < num:
        num_list.append(num)
        max = num
    else:
        continue

print(num_list)
