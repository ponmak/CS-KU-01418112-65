# พิมพ์ดาวบรรทัดเดียวสลับกัน

n = int(input())
char_1 = str(input())
char_2 = str(input())

# printing by no using String Slicing
char_long_size = (char_1 + char_2) * (n//2) + char_1 *(n%2) # CC : leo สุดโหด
print(char_long_size)

# printing by using String Slicing
char_long_size = (char_1 + char_2) * n # สร้าง string ทียาวๆเลย
print(char_long_size[:n]) # แล้วตัดมาเฉพาะตัวถึง n ตัว (เรียนอีกที่ในการใช้ string slice)
