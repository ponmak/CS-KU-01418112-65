# 12 Craps

counter = 1

while True:

    num_1 = int(input())
    num_2 = int(input())

    if (num_1 <= 0 or num_1 >= 7) or (num_2 >= 7 or num_2 <= 0):
        print('ERROR')
        continue
    elif counter == 1 and (num_2 + num_1 == 7 or num_2 + num_1 == 11):
        print(f'{counter} {num_1 + num_2} W')
        break
    elif counter == 1 and (num_2 + num_1 == 2 or num_2 + num_1 == 12 or num_2 + num_1 == 3):
        print(f'{counter} {num_1 + num_2} L')
        break
    elif counter == 1:
        target = num_1 + num_2
    else:
        if num_2 + num_1 == target:
            print(f'{counter} {num_1 + num_2} W')
            break
        elif num_1 + num_2 == 7:
            print(f'{counter} {num_1 + num_2} L')
            break
        
    counter += 1

        

        