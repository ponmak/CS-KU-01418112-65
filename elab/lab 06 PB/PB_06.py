# 06 ผลบวกของหลักเลขจนเหลือหลักเดียว

num = int(input())
temp_num = num
sum_num = 0

while True:
    if temp_num != 0:
        sum_num += temp_num % 10
        temp_num //= 10
    else:
        if sum_num - 10 >= 0:
            temp_num = sum_num
            sum_num = 0
            
            sum_num += temp_num % 10
            temp_num //= 10
        else:
            break

print(sum_num)
