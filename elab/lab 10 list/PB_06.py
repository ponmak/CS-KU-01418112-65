# 06 การเพิ่มข้อมูลเข้าไปใน List

scores = []

scores.append(20) # append เอามาต่อท้ายใน list
print('Scores:', scores)

data = ['a', 'b', 'c', 'e', 'f']

data.append('d')
print('Data:', data)

def factors(number):
    factors = []
    for factor in range(1, number+1):
        if number % factor == 0:
            factors.append(factor)
    return factors

print('Factors of 27 is:', factors(27))

# 1. เขียนโปรแกรมเพื่อรับจำนวนเต็ม จนกว่าผู้ใช้จะพิมพ์ -1 เก็บจำนวนเต็มทุกจำนวนใส่ตัวแปรลิสต์ data ตามลำดับที่รับเข้ามา
# แล้วแสดงข้อมูลในลิสต์ data (แสดงให้แล้ว)
data = []
while True:
    num = int(input())

    if num == -1:
        break
    else:
        data.append(num)

print(data)

# 2. เขียนโปรแกรมเพื่อรับสตริง หยุดรับข้อมูลเมื่อเป็นสตริงว่าง เก็บสตริงทุกค่าใส่ตัวแปรลิสต์ data ตามลำดับที่รับเข้ามา
# แล้วแสดงข้อมูลในลิสต์ data (แสดงให้แล้ว)
data = []
while True:
    str_ = input()

    if str_ == '':
        break
    else:
        data.append(str_)

print(data)



