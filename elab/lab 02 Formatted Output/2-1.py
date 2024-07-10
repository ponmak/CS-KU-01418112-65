# ขั้นระหว่าง  string
print("Hello", "Python") # Output : Hello Python\n จะมีเว้นว่างหรว่างตัวแปรให้เลย

#ขั้นระหว่างตัวแปร
print(34, 24, 35, 170.0) # Output : 34 24 35 170.0\n

#ชั้นต่างชนิดได้
print("I'm", 19, "years old") # Output : I'm 19 years old\n

# ขั้นระหว่างตัวแปรได้
a,b = 17,35
print(a, b) # Output : 17 35\n

#กำหนดช่วงของตัวได้จาก sep='ตัวที่ต้องการ'
print(34, 24, 35, 170.0, sep=',')

print(34, 24, 35, 170.0, sep='')

print("I'm", 19, "years old", sep='-:-')

'''ตามหลัง print() จะเป็น \n เสมอ สามารถกำหนดแบบไม่เว้น
ได้จากการกำหนด print(end='') ให้เหลือแค่ str ตัวเดียว หรือหากตองการเว้นคือทำอะไรลงท้ายก้สามารถทำได้'''

print("I'm", end=' ')
print(19, end='')
print("yrs.", end='\n')