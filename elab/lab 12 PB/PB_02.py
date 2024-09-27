# 02 ใส่ " ใน CSV

text = input()
text_list = []

# spilt the data
temp_str = ""

for i in range(len(text)):
    if text[i] != ",":
        temp_str += text[i]
    else:
        text_list.append(temp_str)
        temp_str = ""

text_list.append(temp_str) # add last text

# strip func my hand
count = 0 # can use like 2d array na but teacher sacc wiil 😡
for word in text_list:
    temp_str = ""

    i = 0
    while i < len(word):
        if word[i] == ' ' and temp_str == "":
            i += 1
        elif (word[i:i+2] == '  ' or i == len(word)-1)and temp_str != "" : # Myself fix this pleaessssss
            #print(f"last format : {temp_str}")
            break
        else:
            temp_str += word[i]
            i += 1

    text_list[count] = temp_str
    count += 1
#print(text_list)

# set "" to all word
mod_text_list = ['"' + word + '"' for word in text_list]

# join method go boom boom
ans = ""
i = 0
while i < len(mod_text_list):
    if i != len(mod_text_list) - 1:
        ans += mod_text_list[i] + ","
    else:
        ans += mod_text_list[i]

    i += 1

# ans = ",".join(mod_text_list) : the easiest way to add ","

print(ans)
