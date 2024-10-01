# 03 ทำ = ให้ตรงกัน

text_list  = []

while True:
    text = input()

    if text == "-1":
        break

    equ_counter = 0
    new_text = ""
    for i in range(len(text)):
        if i+1 < len(text) and text[i] != " " and text[i+1] == '=' and equ_counter == 0:
            new_text += text[i] + ' '
            equ_counter += 1
        elif  i < len(text) and text[i] != " " and text[i-1] == '=' and equ_counter < 2:
            new_text += ' ' + text[i]
            equ_counter += 1
        elif i+1 < len(text) and text[i] == " " and text[i] == text[i+1]:
            pass
        elif text[i] == " " and new_text == '':
            pass
        elif text[i] == '=' and i == 0:
            new_text += '  ' + text[i]
        else:
            new_text += text[i]

    text_list.append(new_text)
#print(text_list)

max_list = []
# find = that between empty space
for i in range(len(text_list)):
    max_before_equal = 0
    for j in text_list[i]:
        if j != '=' :
           max_before_equal += 1
        else:
            max_list.append(max_before_equal)
            break

#print(max_list)
for i in range(len(max_list)):
    if max_list[i] != max(max_list):
        text_list[i] = " "* (max(max_list) - max_list[i]) + text_list[i]

for i in text_list:
    print(i)
