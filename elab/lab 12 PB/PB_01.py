# 01 ทำสระให้เป็นตัวใหญ่

text = input()
ans = ""

for i in text:
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        ans += i.upper()
    else:
        ans += i.lower()
        
print(ans)
