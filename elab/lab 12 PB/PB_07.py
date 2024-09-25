# 07 camelCase

text = input()
ans = ""

i = 0
while i < len(text):
    
    if i == 0 and text[i].isupper():
        ans += text[i].lower()
        i += 1

    if text[i] in ['-','_','=','.','$']:
        j = 0
        
        while True:
            if text[j+i] in ['-','_','=','.','$']:
                j += 1
            else:
                break
            
        ans += text[i+j].upper()
        # print(f"camel case : {ans}, i = {i}, j = {j}")
        i += j + 1
    else:
        ans += text[i]
        i += 1

print(ans)    