# 05 Elab Test Case

sent = input()
standard = input()

Num_sent = -2
count = 0

for i in range(len(sent)):
    if sent[i] in standard:
        count += 1
    Num_sent += 1
    
print(count)
if Num_sent != 0:
    print(f"{(count / Num_sent) * 100 :.2f}")
else:
    print(f"{0:.2f}")