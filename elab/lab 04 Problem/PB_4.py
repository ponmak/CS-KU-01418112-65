#04 Buffet

choice = input('Enter your buffet choice: ')

KOREAN = 1500
JAPANESE = 1000

if choice == 'Korean' or choice == 'korean':
    is_wed = input('Is today Wednesday (yes/no)? ')
    if is_wed == 'yes':
        print(f'Your payment is {KOREAN * (85 / 100):.2f} Baht.')
    else:
        print(f'Your payment is {KOREAN:.2f} Baht.')
elif choice == 'Japanese' or choice == 'japanese':
    is_wed = input('Is today Wednesday (yes/no)? ')
    if is_wed == 'yes':
        print(f'Your payment is {JAPANESE * (85/100):.2f} Baht.')
    else:
        print(f'Your payment is {JAPANESE:.2f} Baht.')
else:
    print(f'Sorry, there is no {choice} buffet.')
