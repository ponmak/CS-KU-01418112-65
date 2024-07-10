# ฟังก์ชันทางคณิตศาสตร์ : Method และ Library

# library คือการใช้เรียกสิ่่งที่ python ปกติไม่สามารถทำได้  
import math 
# การเรียกใช้func ต้อ'ใช้ ชื่อ lib แล้ว . ตามด้วย method ตามต้อการ

x = float(input('Enter x: '))
y = float(input('Enter y: '))
z = float(input('Enter z: '))

print(f'a1 = {math.pow(x,y) + z:.2f}') # การใช้ method บ้าง method ต้องใส่ค่าใน()ให้ครบ(ตามที่กำหนดอะนะ) 
# หากเอาเมาส์ไปชี้สามารถดูได้ว่าใน () ต้องการค่่าไรบ้าง 
print(f'a2 = {math.cos(2 * math.pi) + math.log(x):.2f}') # อย่างข้อนี้ไม่ต้องใส่ค่าใน log ไม่ครบก็ได้เพราะมันจะกำหนดเป็นฐาน e อยู่แล้ว
print(f'a3 = {abs(x) + abs(y):.2f}') # บ้าน func อาจจะไม่อยุ่ใน lib จะสามารถเรียกใช้ได้เลย
print(f'a4 = {math.sqrt(x**2 + y**2 + z**2):.2f}')

# Extra 
#เราสามารถกำหนด library เป็น parameter ได้จากการเขียน as ตามท้าย อาจะทำให้เข้าใจยากแต่ทำให้ code นั้นกระชับขึ้นอย่างมาก

import math as m # ที่นี้เราสามารถเรียกตัวแปรจาก m ได้เลย

print(f'a5 = {(m.sin(x)**2) + (m.cos(x)**2):.2f}')
print(f'a6 = {m.exp(m.log(x+y)/5):.2f}')
print(f'a7 = {m.e ** (x * m.log(y)):.2f}')
