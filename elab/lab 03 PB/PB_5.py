target = 72

NUM = int(input('Enter your guess (0 - 100): ')) 

if NUM == target and NUM >= 0 and NUM <=100 :
    print('Congratulations, your guess is correct.')
elif NUM >= 0 and NUM <=100 and NUM != target:
    print('Sorry, your guess is wrong, try again later.')
else:
    print('Sorry, out of range, try again later.')