# 01 Repetition: while

# Exercise 1 เขียน while loop เพื่อพิมพ์จำนวนคู่ตั้งแต่ 1 ถึง 100 จากน้อยไปมาก บรรทัดละจำนวน

i = 1 
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1

# Exercise 2 เขียน while loop เพื่อพิมพ์จำนวนคี่ตั้งแต่ 100 ถึง 50 จากมากไปน้อย บรรทัดละจำนวน 

i = 100
while i > 50:
    if i % 2 != 0:
        print(i)
    i -= 1

# Exercise 3 รับจำนวนเต็มบวก 1 จำนวน
# เขียน while loop เพื่อพิมพ์จำนวนที่หารด้วย 3 ลงตัว ตั้งแต่ 0 ถึง 
# จำนวนที่รับเข้ามา จากน้อยไปมาก บรรทัดละจำนวน

i = int(input())
counter = 0
while counter < i:
    if counter % 3 == 0:
        print(counter)
    counter += 1

# Exercise 4 รับจำนวนเต็มบวก 1 จำนวน
# เขียน while loop เพื่อนับจำนวนที่หารด้วย 3 ไม่ลงตัว ตั้งแต่ 0 ถึง จำนวนที่รับเข้ามา
# พิมพ์จำนวนที่นับได้

i = int(input())
j = 0
counter = 0
while j <= i:
    if j % 3 != 0:
        counter += 1
    j += 1
print(counter)

# Exercise 5
# Input: รับจำนวนเต็มบวก 1 จำนวน แทนด้วย n
# จากนั้นรับจำนวนจริงอีก n บรรทัด แทนคะแนนสอบของนักเรียน n คน
# Process: เขียนโปรแกรมเพื่อคำนวณค่าเฉลี่ยของคะแนนสอบจากข้อมูลที่รับเข้ามา และนับจำนวนนักเรียนที่ได้คะแนนสอบมากกว่า 40 ว่ามีกี่คน
# Output: มีบรรทัดเดียว ประกอบด้วย ค่าเฉลี่ย (ทศนิยม 2 ตำแหน่ง) ของคะแนนสอบของนักเรียน n คน และจำนวนนักเรียนที่ได้คะแนนสอบมากกว่า 40 คะแนน คั่นด้วยเว้นวรรค

num = int(input())
sum_stu = 0
more_than_40 = 0
i = 0
while True:
    if i == num:
        break
    else:
        s_stu = float(input())
        if s_stu > 40:
            more_than_40 += 1
            sum_stu += s_stu
            i += 1
        else:
            sum_stu += s_stu
            i += 1

print(f'{sum_stu / num:.2f} {more_than_40}')

