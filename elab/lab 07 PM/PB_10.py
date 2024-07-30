# 10 Sum odd digits
num = input()

s_odd = 0

i = 0
while i < len(num):
    if int(num[i]) % 2 != 0:
        s_odd += int(num[i])
    else:
        pass
    i += 1

if s_odd == 0:
    print(-1)
else:
    print(s_odd)