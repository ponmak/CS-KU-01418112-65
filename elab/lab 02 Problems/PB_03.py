#พิมพ์ตามสั่ง

# input : float inc และ float ex
inc = float(input()) #Total Income
ex = float(input()) #Expense

# output
print("1234567890" * 3)

# using f'' 
print(f'{"Total Income": <13} {inc:>+8.2f} bahts')
print(f"{"Expense": <13} {ex:>-8.2f} bahts")
print(f"{"Profit": <13} {inc + ex:>08.2f} bahts")

# {: <13} mean จองพื้นที่ 13 ตัวอักษร จากฝั่งซ้าย
# {:+8.2f} mean จองพื้นที่ 8 ตัวอักษร จากฝั่งขวา และมี 2 ตำแหน่งทศนิยม
# {:-8.2f} mean จองพื้นที่ 8 ตัวอักษร จากฝั่งขวา และมี 2 ตำแหน่งทศนิยม
# {:>08.2f} mean จองพื้นที่ 8 ตัวอักษร จากฝั่งขวา และมี 2 ตำแหน่งทศนิยม
# {:<13} mean จองพื้นที่ 13 ตัวอักษร จากฝั่งซ้าย