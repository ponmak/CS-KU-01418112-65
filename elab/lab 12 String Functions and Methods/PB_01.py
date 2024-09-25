# 01 String Functions

# len(string) : หาความยาว str

'''
Ex.1 เขียนโปรแกรมรับค่าสตริงจาก standard input บรรทัดละค่าจนกว่าจะเป็นสตริงว่าง
แล้วแสดงผลลัพธ์ว่าสตริงค่าที่มีความยาวมากที่สุด มีความยาวเท่าใด
'''
word_list = []

while True:
    text = input()
    
    if text == "":
        break
    
    word_list.append(len(text))
    
print(max(word_list))

'''
Ex.2 เขียนโปรแกรมรับค่าสตริงจาก standard input บรรทัดละค่าจนกว่าจะเป็นสตริงว่าง แล้วแสดงผลลัพธ์ว่าสตริงค่าที่มีความยาวมากที่สุด คือสตริงค่าใด
'''

word_list = []

while True:
    text = input()
    
    if text == "":
        break
    
    word_list.append(text)
    
inx_word_list = []

for i in word_list:
    inx_word_list.append(len(i))
    
for i in range(len(word_list)):
    if max(inx_word_list) == inx_word_list[i]:
        print(word_list[i])