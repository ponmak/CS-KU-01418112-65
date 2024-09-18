# 02 String Operators 2 Indexing

# 1. Indexing (Access Index of String)
# Opertor : []

print('Python'[0])

subject = 'Fundamental Programming Concept'
text = subject[27] + subject[14] + subject[5] + subject[29] + subject[1] + subject[30] + subject[28] + subject[16]
print(text)

subject = 'Fundamental Programming Concept'
text = subject[-22] * 5 + subject[0] * 0
print(text)

# 2. String index out of range

subject = 'Fundamental Programming Concept'
print(subject[31]) # out of range ได้เหมือน list

# 3. Strings are immutable! 
s = "Strings are immutable!"
s[-1] = '.' # ไม่สามารถเปลี่ยนแปลงค่าได้เหมือน list
print(s)