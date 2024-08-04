# 03 Guessing 3

counter = 0
target  = 72

while True:
    
    NUM_GUSESS = int(input('Enter your guess: '))
    
    if NUM_GUSESS < 0 or NUM_GUSESS > 100 : 
        print('Sorry, your guess is out of range.')
        counter += 1
    elif NUM_GUSESS == target :
        print('Congratulations, your guess is correct.')
        counter += 1
        break
    elif NUM_GUSESS < target :
        print('Sorry, your guess is too low.')
        counter += 1
    else :
        print('Sorry, your guess is too high.')
        counter += 1

print(f'Total number of guesses is {counter}.')