# 01 List Methods 1 

# append(data), 
# extend(data:iterable) : list to list no return var
# insert(index, data)

# Ex.1 เขียนโปรแกรมเพื่อรับข้อมูลเข้าบรรทัดละค่า 
# หยุดรับข้อมูลเมื่อเป็นสตริงว่าง เก็บข้อมูลเข้าไปใน List ls

ls = []
while True:
    text = input()

    if text == '':
        break

    ls.append(text)

# Ex.2 จงเขียน function definition ของฟังก์ชัน create_factors_3_7(n) 
# ที่รับ parameter เป็นจำนวนเต็มบวก n
# ฟังก์ชันนี้จะคืนค่า List ที่ประกอบด้วย จำนวนเต็มบวกที่มี 3 หรือ 7 เป็นตัวประกอบ 
# เรียงลำดับจากน้อยไปมาก จำนวน n ตัว

def create_factors_3_7(n):
    ls = []
    i = 1
    while len(ls) < n:
        if i % 3 == 0 or i % 7 == 0:
            ls.append(i)
        i += 1
    return ls

