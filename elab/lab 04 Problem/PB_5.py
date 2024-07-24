# 05 มาตรการเงินโอน แก้จน คนขยัน

age = int(input('Enter your age: '))
income = int(input('Enter your net income: '))

if 15 <= age and age <= 60 and income > 0 and income < 80000:
    if 1 <= income <= 30000:
        print(f'Your negative income tax is {income * (20/100):.2f} Baht.')
    else:
        print(f'Your negative income tax is {(80000 - income) * (12/100):.2f} Baht.')
elif age < 15 or age > 60:
    print('Invalid age.')
else:
    print('Invalid income.')