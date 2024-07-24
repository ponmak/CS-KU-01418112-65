#03 Electric Appliance Store

TV_num = int(input('How many TVs? '))
DVD_num = int(input('How many DVD players? '))
AS_num = int(input('How many Audio Systems? '))

total = (TV_num * 6000) + (DVD_num * 1500) + AS_num * 3000
print(f'Total price is {total:.2f} baht.')

if total < 24000:
    print(f'Your payment is {total:.2f} baht. Thank you!')
else:
    print(f"You've got a discount of {total * (20/100):.2f} baht.")
    print(f'Your payment is {total * (80/100):.2f} baht. Thank you!')