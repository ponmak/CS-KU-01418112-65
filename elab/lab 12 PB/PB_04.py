# 04 ชื่อไฟล์ที่ถูกต้อง

DOUSETEXT = ['\\', '/', '*', ':', '|', '"','<', '>']

text = input()

find_dot_ind = text.rfind('.')

front_text = text[:find_dot_ind]
back_text = text[find_dot_ind:]

# behind dot section
behind_dot = "."

for i in back_text:
    if i in DOUSETEXT or i == ' ':
        i = '_'
        behind_dot += i
    elif i == '.' and i in '.':
        pass
    else:
        behind_dot += i

#print(behind_dot[:4])

if find_dot_ind == -1:
    front_text = text
    behind_dot = ''

# front dot section
front_dot = ""

i = 0
while i < len(front_text):

    if i == 15:
        break

    if front_text[i] in DOUSETEXT or front_text[i] == '.' or front_text[i] == ' ':
        front_dot += "_"
    else:
        front_dot += front_text[i]

    i += 1

print(front_dot+behind_dot[:4])
