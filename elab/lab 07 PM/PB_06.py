# 06 ตรวจสอบสามเหลี่ยมมุมฉาก

import math

a = int(input())
b = int(input())
c = int(input())

if c == math.sqrt(a**2 + b**2):
    print(True)
elif a == math.sqrt(b**2 + c**2):
    print(True)
elif b == math.sqrt(c**2 + a**2):
    print(True)
else:
    print(False)
