# 03 ทอนเงิน (ธนบัตรใดๆ)

def change(money: int,bank: int) -> int : # copy for lab 08 PB
    return money // bank

n = int(input())

bank = [] # คิอชื่อไม่ออก
for i in range(n):
    bank.append(int(input()))
bank.sort(reverse=True)

money_in = int(input())
ans = []

for i in bank:
    temp = change(money_in, i)
    ans.append(temp)
    money_in = money_in - temp*i

for i in range(len(bank)):
    print(f"{bank[i]}: {ans[i]}")
