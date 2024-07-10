#String Interpolation Operator : % (hardest not a zen of python)

#by using % operator : %s for string, %d for integer, %f for float
output = "%s, %s %s." % ("Hello", "Python", "is easy")
print(output)

# can custom parameter by using %10.2f mean จองพื้นที่ 10 ตัวอักษร จากฝั่งขวา และมี 2 ตำแหน่งทศนิยม
output = "Width: %.2f,Height: %10.2f\\Age: %d." % (55, 171.2658, 19)
print(output)