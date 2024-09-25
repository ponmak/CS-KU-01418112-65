# 04 String Methods 1

# str.islower/isupper : return bool ,is all text is lower/upper

"""
Ex.1 เขียนโปรแกรมรับสตริงมา 1 ค่า แล้วแสดงผล 2 บรรทัด
บรรทัดแรกแสดงจำนวนตัวอักษรที่เป็นตัวเล็กในสตริง 
บรรทัดที่สองแสดงจำนวนตัวอักษรที่เป็นตัวใหญ่ในสตริง
"""
text = input()

l_count = 0
u_count = 0

for i in text:
    if i.isupper():
        u_count += 1
    elif i.islower():
        l_count += 1
        
print(l_count)
print(u_count)

# .upper/lower : change all upper/lower to other

text = input()

ans = ""

for i in text:
    if i.isupper():
        ans += i.lower()
    elif i.islower():
        ans += i.upper()
    else:
        ans += i 
print(ans)