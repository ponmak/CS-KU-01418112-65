# 06 List and String 2 

#  .join(ls)
ls = []
ans = ""
while True:
    text = input()

    if text == '':
        break
    ls.append(text)
print(ans.join(ls))
