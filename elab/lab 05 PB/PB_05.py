# 05 Triangle of 1s

lines = int(input('Enter height: '))
inves_lines = 0
counter = 0
counter_2 = 1
while counter < lines:
    print(' ' * (lines - counter - 1)*2 + '1', end='')
    if counter == 0:
        print(' ' * inves_lines)
        inves_lines = 3
    elif counter == 1:
        print(' ' * (counter* inves_lines) + '1')
    else:
        print(' ' * (counter* inves_lines + counter_2 ) + '1')   
        counter_2 += 1 
    counter += 1
