# Boolean Expression: Logical Operators

# Logical Operators
# จะเชื่อมระหว่าง Boolean เท่านั้น Data Type อื่น จะถูกแปลงเป็น Boolean ก่อน

# and, or, not

print(True and True) # output : True

print(False or False) # output : False

import math
r = 3 
print(math.pi == 3.14 and r > 0 and r < 5) # output : False

a = 150
print( a % 4 == 0 or a % 3 == a % 5 ) # output : True

y1 = -403
y2 = -522
print( not abs(y2 - y1) > 0 ) # output : False

x = ''
if x != 'a' or x != 'b':  # output : True เนื่องจาก x จะเป็นจริงตลอด
    print(True)

'''n ต้องมีค่าไม่น้อยกว่า 0 และต้องมีค่าไม่มากกว่า 100 ถ้า n ไม่อยู่ในช่วงนี้จะพิมพ์ว่า Error
if n < 0 and n > 100:  '''
n = 1
if n < 0 and n > 100: # output : False
    print(True)
else:
    print(False)
    
# ต้องการตรวจสอบว่า n อยู่ในช่วงปิด [0, 100] หรือไม่
n = 0
if n >= 0 or n <= 100:  
    print(True)
else:
    print(False) # output : True
    
# ต้องการตรวจสอบว่า ch ต้องเป็นอักขระ 'a' หรืออักขระ 'b' หรืออักขระ 'c' เท่านั้น
ch = 'a'
if ch == 'a' or 'b' or 'c': # output : True
    print(True)