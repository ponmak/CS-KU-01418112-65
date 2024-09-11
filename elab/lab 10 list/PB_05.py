# 05 ฟังก์ชัน range()

# range(start, stop, step )

# start เริ่มจากตัวที่ n เอาตัวมันเองด้วย
# stop หยุดจนlist มีจำนวน n
# step ข้ามที่ละ n ค่า

# 1. range(stop) เป็นการเรียนค่าจำนวนจริงตั้งแต่ 0 ถึง number-1
print(list(range(20))) # output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

numbers = list(range(20))
print(numbers[4] + numbers[7]) # output : 11

# 2. range(start, stop)
print(list(range(10, 30))) # output : [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

numbers = list(range(10, 30))
print(numbers[4] + numbers[7]) # output : 31

# 3. range(start, stop, step)
print(list(range(1, 20, 2))) # output : [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

numbers = list(range(1, 20, 2))
print(numbers[4] + numbers[7]) # output : 24

# step สามารถถอยหลังได้เหมือนกัน
print(list(range(20, 10, -1))) # output : [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

# 1. ใช้ For Loop ในการเข้าถึงด้วย Index แล้วแสดงข้อมูลทีละบรรทัด โดยใช้ range
scores = [60, 70, 85, 66, 70, 0, 15, 9]
for i in range(len(scores)):
    print(scores[i])
