#สระว่ายน้ำ
width = float(input("Enter width: ")) #รับค่าเป็นทศนิยม
length = float(input("Enter length: "))
depth = float(input("Enter depth: "))

Aear = width * length * depth

#f'' เพื่อความง่าย
print(f'Time to fill a pool is {(Aear * 15) / 60:.2f} minutes.')  #คำนวณเวลาที่ใช้ในการเติมน้ำเข้าสระว่ายน้ำ