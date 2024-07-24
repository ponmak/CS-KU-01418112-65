# 02 เมนู
 
print('---<< Main Menu >>---')
print('    <B>urger Meal')
print('    <C>hicken Meal')
print('    <P>asta Meal')


choice = input('Enter your choice: ').upper()

if choice == 'B':
    print('---<< Burger Sub Menu >>---')
    print('    <R>egular Burger')
    print('    <C>heese Burger')
    print('    <D>ouble Cheese Burger')
    
    B_choice = input('Enter your choice: ').upper()
    
    if 'R' == B_choice:
        print('Your Regular Burger is 60 Baht.')
    elif 'C' == B_choice:
        print('Your Cheese Burger is 75 Baht.')
    elif 'D' == B_choice:
        print('Your Double Cheese Burger is 90 Baht.')
    else:
        print('Invalid sub menu choice.')
elif choice == 'C':
    print('---<< Chicken Sub Menu >>---')
    print('    <F>ried Chicken    ')
    print('    <G>rilled Chicken    ')
    print("    <C>hef's Chicken    ")

    C_choice = input('Enter your choice: ').upper()

    if 'F' == C_choice:
        print('Your Fried Chicken is 120 Baht.')
    elif 'G' == C_choice:
        print('Your Grilled Chicken is 150 Baht.')
    elif 'C' == C_choice:
        print("Your Chef's Chicken is 180 Baht.")
    else:
        print('Invalid sub menu choice.')
elif choice == 'P':
    print('---<< Pasta Sub Menu >>---')
    print('    <S>paghetti de Italiano    ')
    print('    <L>asagna Supreme    ')
    print('    <M>acaroni Special    ')

    p_choice = input('Enter your choice: ').upper()

    if 'S' == p_choice:
        print('Your Spaghetti de Italiano is 90 Baht.')
    elif 'L' == p_choice:
        print('Your Lasagna Supreme is 120 Baht.')
    elif 'M' == p_choice:
        print('Your Macaroni Special is 100 Baht.')
    else:
        print('Invalid sub menu choice.')
else:
    print('Invalid main menu choice.')

    