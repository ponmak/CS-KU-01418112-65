#Formatted String Literal : fstring (easiest and most powerfull)

# by using f"" using like normal string but have format 

#using parameter inside bracket
price = 12.55
output = f"Price in Euro: {price}"
print(output)

# can custom parameter
price = 12.54
output = f"Price in Swiss Franks: {price * 1.086}"
print(output)

# :10.2f mean จองพื้นที่ 10 ตัวอักษร จากฝั่งขวา และมี 2 ตำแหน่งทศนิยม
price = 12.54
rate = 1.086
output = f"Price in Swiss Franks: {price * rate:10.2f}"
print(output)