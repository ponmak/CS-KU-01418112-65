# 04 คำสั่ง for

'''1. ประกาศ List ของจำนวนเฉพาะ ให้ชื่อตัวแปรว่า primes โดยมีข้อมูลเป็นจำนวนเฉพาะ 10 จำนวนแรก
คำนวณหาผลรวมของจำนวนเฉพาะทั้ง 10 จำนวน โดยใช้ for loop เก็บผลรวมใส่ในตัวแปร total'''

primes = [2,3,5,7,11,13,17,19,23,29]
total = 0
for i in primes: # เราสามารถดึงค่าจาก primes ลงใน i แล้ว loop จาก for ได้
    total += i
print(total)

'''2. ให้เขียนฟังก์ชัน find_max ที่รับ parameter list ซึ่งเป็นลิสต์ของจำนวนเต็ม เพื่อหาค่าที่มากที่สุดในลิสต์ list ที่รับเข้ามา โดยใช้ for loop ในการหา แล้วคืนค่าที่มากที่สุดนั้น'''
import math
def find_max(list):
    max = -(math.inf)
    for i in list:
        if i > max:
            max = i
    return max

print(find_max([1, 2, 3, 4]))
print(find_max([4, 3, 2, 1]))
print(find_max([4, 3, 5, 9, 7, 2, 4, 4, 10, 0, 11, 8]))
print(find_max([-7, -9, -8, -2, -7, -11, -4, -5]))