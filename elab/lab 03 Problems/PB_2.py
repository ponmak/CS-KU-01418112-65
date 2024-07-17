AMOUNT = float(input('Enter buying amount: '))

if AMOUNT >= 1000 and AMOUNT < 3000:
    print(f'Amount due after discount is {AMOUNT * (90/100):.2f} baht.')
elif AMOUNT >= 3000:
    print(f'Amount due after discount is {AMOUNT * (85/100):.2f} baht.')
else:
    print(f'Amount due after discount is {AMOUNT:.2f} baht.')