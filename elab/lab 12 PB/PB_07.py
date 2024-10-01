# 07 camelCase

text = input()
ans = ""
first_temp = ''
first_upper = True

i = 0
while i < len(text):

    if len(ans) < 2 and ans.isupper() and first_upper:
        ans = ans.lower()
        first_upper = False

    elif text[i] in ['-','_','=','.','$',' ']:
        j = 1

        while i+j < len(text) and text[i+j] in ['-','_','=','.','$',' ']:
            j += 1

        if i + j < len(text):
            ans += text[i + j].upper()

        i += 1 + j
    else:
        ans += text[i].lower()
        i += 1

    #print(ans)
print(ans)
