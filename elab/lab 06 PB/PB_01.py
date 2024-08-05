# 01 Master Mind

TARGET = int(input('Enter a target (4-digit integer): '))
GUESS = int(input('Enter your guess (4-digit integer): '))

target_range_counter = 0
guess_range_counter = 0

# correct
digits = 0
position = 0

target_temp = TARGET

if TARGET == GUESS:
    print('Congratulations, you just mastered my mind!!')
else:
    while target_range_counter < 4:
        
        mod_tar = target_temp % 10
        target_temp //= 10

        # init for new loop
        guess_temp = GUESS
        guess_range_counter = 0
        
        while guess_range_counter < 4:
            mod_guess = guess_temp % 10
            guess_temp //= 10
            if mod_tar == mod_guess and target_range_counter == guess_range_counter:
                position +=1
                pass
            elif mod_tar == mod_guess and target_range_counter != guess_range_counter:
                digits += 1
                pass
            else:
                pass
            guess_range_counter += 1
        target_range_counter +=1
    
    digits_ref = digits
    position_ref = position

    if digits == 0:
        digits = 'no'
    elif digits == 1:
        digits = 'one'
    elif digits == 2:
        digits = 'two'
    elif digits == 3:
        digits = 'three'
    else:
        digits = 'four'

    if position == 0:
        position = 'No'
    elif position == 1:
        position = 'One'
    elif position == 2:
        position = 'Two'
    elif position == 3:
        position = 'Three'
    else:
        position = 'four'
 

    if (position_ref > 1 and digits_ref > 1) or (position_ref == 0 and digits_ref == 0):
        print(f'{position} positions correct, {digits} digits correct')
    elif position_ref == 1 and digits_ref != 1:
        print(f'{position} position correct, {digits} digits correct')
    elif position_ref != 1 and digits_ref == 1:
        print(f'{position} positions correct, {digits} digit correct')
    elif  position_ref == 1 and digits_ref == 1:
        print(f'{position} position correct, {digits} digit correct')  
    else:
        print(f'{position} positions correct, {digits} digits correct')