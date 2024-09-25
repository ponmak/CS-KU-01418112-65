# 02 String Functions 2

# ord(char) : char to ascii num
# chr(int) : assci num to char

"""
Ex.1 เขียนโปรแกรมรับค่า 2 บรรทัด จาก standard input บรรทัดแรกเป็นตัวอักษร ch 1 ตัว
บรรทัดที่ 2 รับจำนวนเต็ม n 1 จำนวน แล้วแสดงผลลัพธ์เป็นตัวอักษรที่ถัดไปจาก ch อีก n ตัว
ตามตารางแอสกี้
"""

text = input()
num = int(input())

print(chr(ord(text) + num))
