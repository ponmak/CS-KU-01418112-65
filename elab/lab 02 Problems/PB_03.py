#พิมพ์ตามสั่ง

# input : float inc และ float ex
inc = float(input()) #Total Income
ex = float(input()) #Expense

# output
print("1234567890" * 3)

# using f''
print(f'{"Total Income": <13} {inc:>+8.2f} bahts')
print(f"{"Expense": <13} {ex:>-8.2f} bahts")
print(f"{"Profit": <13} {inc + ex:>08.2f} bahts")
