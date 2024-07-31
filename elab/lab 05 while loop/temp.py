num = int(input())
sum_stu = 0
more_than_40 = 0
i = 0
while True:
    if i == num:
        break
    else:
        s_stu = int(input())
        if s_stu > 40:
            more_than_40 += 1
            sum_stu += s_stu
            i += 1
        else:
            sum_stu += s_stu
            i += 1

print(f'{sum_stu / num:.2f}',f'{more_than_40}')