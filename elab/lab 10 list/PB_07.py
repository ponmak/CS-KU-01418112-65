# 07 List Functions

scores = [60, 70, 85, 66, 70, 0, 15, 9]
number_of_scores = len(scores)
print(number_of_scores)

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print( 'There are', len(days), 'days in a week.' )

print(len([]))

scores = [60, 70, 85, 66, 70, 0, 15, 9]
total = sum(scores)
print(total)

scores = [60, 70, 85, 66, 70, 0, 15, 9]
max_score = max(scores)
print(max_score)

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print( max(days) )

scores = [60, 70, 85, 66, 70, 0, 15, 9]
min_score = min(scores)
print(min_score)

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print( min(days) )

'''1. เขียนโปรแกรมเพื่อรับสตริง หยุดรับข้อมูลเมื่อเป็นสตริงว่าง เก็บสตริงทุกค่าใส่ตัวแปรลิสต์ data ตามลำดับที่รับเข้ามา
แล้วแสดงสตริงที่มีจำนวนอักขระมากที่สุด'''
data = []

while True:
    str_= input()

    if str_ == '':
        break
    else:
        data.append(str_)

max = ''
for i in data:
    if len(max) < len(i):
        max = i

print(max)