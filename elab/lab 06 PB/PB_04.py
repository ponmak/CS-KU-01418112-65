# 04 โบว์ลิง

score = 0
i = 1
spare_left = 0
spare_turn = 0

while i < 11:
    print(f'Frame # {i}')

    if spare_left == 0 and spare_turn == 0:
        pin_down = int(input(f'  Number of pins down: '))

        spare_left = 10 - pin_down 

        if spare_left == 0 :
            score += 10
        else:
            spare_turn += 1

        #print(f'  Now score : {score}')
    else:
        pin_down = int(input(f'  Number of pins down (0-{spare_left}): '))
        spare_left_prev = spare_left
        spare_left = spare_left - pin_down 

        if spare_left == 0 :
            score += 10
            spare_turn += 1
        elif spare_left != 0:
            #print(f'  (!) score need to plus : {10 - spare_left_prev + pin_down}')
            score += 10 - spare_left_prev + pin_down
            spare_turn += 1 

        #print(f'  Now score : {score}')
    
    if spare_turn == 0 or spare_turn == 2:
        #print('(+) restart para')
        spare_turn = 0
        spare_left = 0
        i += 1
    else:
        i = i

print(f'Total score is {score}')
