# 03 String Operators 3 Slicing

# 1. Slicing 

# Operator: [:] // เอาแค่ช่วงถึงตัวนั้นมา

subject = 'Fundamental Programming Concept'
text = subject[12:23]
print(text)
print(subject)

subject = 'Fundamental Programming Concept'
text = subject[-19:-8]
print(text)
print(subject)

# 2. Slicing with Step
# Operator: [::]

# [start:stop:step]

subject = "Fundamental Programming Concept"
print(1, subject[12:23])
print(2, subject[12:23:1])
print(3, subject[12:23:2])

subject = "Fundamental Programming Concept"
print(1, subject[-19:-8])
print(2, subject[-19:-8:1])
print(3, subject[-19:-8:2])

# 3. Slicing with Negative Step

subject = "Fundamental Programming Concept"
print(1, subject[12:23])
print(2, subject[12:23:-1])
print(3, subject[12:23:-2])

subject = "Fundamental Programming Concept"
print(1, subject[22:11])
print(2, subject[22:11:-1])
print(3, subject[22:11:-2])

subject = "Fundamental Programming Concept"
print(1, subject[:23:])
print(2, subject[:23:2])
print(3, subject[22::-1])