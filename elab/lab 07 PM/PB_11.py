# 11 Product even digits

num = input()

m_even = 1
s_even = 0

i = 0
while i < len(num):
    if int(num[i]) % 2 == 0:
        m_even *= int(num[i])
        s_even += int(num[i])
    else:
        pass
    i += 1

if s_even == 0:
    print(-1)
else:
    print(m_even)