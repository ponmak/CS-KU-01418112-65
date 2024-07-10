#Area of a circle with radius

import math # import math เพื่อใช้ค่า pi 
# การเรียกใช้ค่า pi  ต้อใช้ ชื่อ lib ตามด้วย method ตามต้อการ

r = int(input("Enter a radius: ")) # เขียน prompt ตามโจทย์ด้วนนะ

Area = (r**2)*math.pi
Circumference = 2 * math.pi * r

#f srting
print(f'Area of a circle with radius {r} is {Area:.2f}')
print(f'Circumference of a circle with radius {r} is {Circumference:.2f}')

# .format
print('Area of a circle with radius {r} is {Area:.2f}'.format(r=r,Area=Area))
print('Circumference of a circle with radius {r} is {Circumference:.2f}'.format(r=r,Circumference=Circumference))

