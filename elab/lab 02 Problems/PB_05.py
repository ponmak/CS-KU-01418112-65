# เติมน้ำมัน

# length and volume
km = int(input())
volume = int(input())

# คำนวณเวลาที่ใช้ในการเติมน้ำเข้าสระว่ายน้ำ
cup_times = km / (15 * volume * (50/100)) # แก้ว
hair_times = km / (15 * volume * (90/100)) # ขวัญ

print(int(cup_times) + 1) 
print(int(hair_times) + 1)

