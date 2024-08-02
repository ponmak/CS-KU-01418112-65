# 01 Master Mind

TARGET = int(input('Enter a target (4-digit integer): '))
GUESS = int(input('Enter your guess (4-digit integer): '))

target_range_counter = 0
guess_range_counter = 0

# correct
digits = 0
position = 0

target_temp = TARGET
guess_temp = GUESS

if TARGET == GUESS:
    print('Congratulations, you just mastered my mind!!')
else:
    while target_range_counter < 4:
        mod_tar = target_temp % 10
        target_temp //= 10
        guess_range_counter = 0
        while guess_range_counter < 4:
            mod_guess = guess_temp % 10
            guess_temp //= 10

            if mod_tar == mod_guess and target_range_counter == guess_range_counter:
                digits += 1
                position +=1
                pass
            elif mod_tar == mod_guess and target_range_counter != guess_range_counter:
                digits += 1
                pass
            else:
                pass
            target_range_counter +=1
            guess_range_counter += 1

print(position,digits)