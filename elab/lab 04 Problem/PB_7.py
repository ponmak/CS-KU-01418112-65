# 07 จับโปเกมอน

lv_pokemon = int(input('Enter level pokemon: '))
lv_pokeball = input('Enter level pokeball: ').upper()
distance = int(input('Enter distance: '))

if lv_pokeball == 'L':
    if 0 <= lv_pokemon <= 40:
        ball_and_lv = 0.05
    elif 41 <= lv_pokemon <= 60:
        ball_and_lv = 0.03
    else:
        ball_and_lv = 0.1
elif lv_pokeball == 'M':
    if 0 <= lv_pokemon <= 40:
        ball_and_lv = 0.03
    elif 41 <= lv_pokemon <= 60:
        ball_and_lv = 0.05
    else:
        ball_and_lv = 0.08
elif lv_pokeball == 'H':
    if 0 <= lv_pokemon <= 40:
        ball_and_lv = 0.01
    elif 41 <= lv_pokemon <= 60:
        ball_and_lv = 0.01
    else:
        ball_and_lv = 0.01
    

s = 100 - (lv_pokemon * ball_and_lv * distance)

if s >= 0:
    print(f'{s:.2f} percent.')
else:
    print('0.00 percent.')

