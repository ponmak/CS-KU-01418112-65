# Guessing 2

NUM_GSESS = int(input('Enter your guess (0 - 100): '))

target  = 72

if NUM_GSESS < 0 or NUM_GSESS > 100 : 
    print('Sorry, out of range, try again later.')
elif NUM_GSESS == target :
    print('Congratulations, your guess is correct.')
elif NUM_GSESS < target :
    print('Sorry, your guess is too low, try again later.')
else :
    print('Sorry, your guess is too high, try again later.')