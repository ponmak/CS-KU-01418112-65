# 03 แทนค่าตัวแปร

var_val = {}

print("Enter variables and values:")
while True:
    text = input()
    if text == "-1":
        break
    [var, val] = text.split('=')
    val = val.strip()
    var = var.strip()
    var_val[var] = val
    
lines = []
print("Enter your program:")
while True:
    text = input()
    if text == "-1":
        break
    for var in var_val:
        key = '{' + var + '}'
        text = text.replace(key, var_val[var])
    lines.append(text)
print("Result:")
for line in lines:
    print(line)