# 07 camelCase

text = input()
ans = ""

i = 0
while i < len(text):

    if i == 0 and text[i].isupper():
        ans += text[i].lower()
        i += 1
        continue

    if text[i] in ['-','_','=','.','$']:
        j = 1

        while i+j < len(text) and text[i+j] in ['-','_','=','.','$']:
            j += 1

        if i + j < len(text):
            ans += text[i + j].upper()

        i += 1 + j
    else:
        ans += text[i].lower()
        i += 1

print(ans)
