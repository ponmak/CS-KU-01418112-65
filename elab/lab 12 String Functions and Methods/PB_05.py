# 05 String Methods 2

'''
Ex.1 เขียนโปรแกรมเพื่อรับข้อมูลเข้า และแสดงข้อมูลออก โดยพิจารณาจากตัวอย่างข้อมูลเข้า/ข้อมูลออกต่อไปนี้
'''

text = input()
find_n_replace = input()
new_replace = input()

print(text.find(find_n_replace))
print(text.count(find_n_replace))
print(text.replace(find_n_replace, new_replace))