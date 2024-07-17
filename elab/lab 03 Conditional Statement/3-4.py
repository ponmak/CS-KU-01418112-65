C = float(input())
F_or_K = str(input())

if F_or_K == 'F' or F_or_K == 'f':
    print( (9/5) * C + 32)
elif F_or_K == 'K' or F_or_K == 'k' :
    print(C + 273.15)
else:
    print('ERROR')