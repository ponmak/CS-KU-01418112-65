# 03 String Functions 3

# max(str) : find max ascii num in str
# min(str) : find min ascii num in str

"""
Ex.1 เขียนโปรแกรมรับสตริงบรรทัดละค่า จนกว่าผู้ใช้จะใส่สตริงว่าง
แสดงผลลัพธ์บรรทัดเดียวเป็นสตริงที่นำตัวอักษรที่มีค่า ascii มากที่สุดจากบรรทัดคี่ มาต่อกับตัวอักษรที่มีค่า
ascii น้อยที่สุดจากบรรทัดคู่ สลับกันบรรทัดละตัวอักษร
"""

ans = ""

count = 1

while True:
    text = input()
    
    if text == "":
        break
    
    if count % 2 == 0:
        ans += min(text)
    else:
        ans += max(text)
        
    count += 1       
print(ans)
        
    
    