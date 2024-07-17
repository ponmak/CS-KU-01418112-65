import math


x = float(input('Enter x : '))

if x < 0:
    y = (x**2 + 1)** (1/2) 
    plb = f'f({x:.2f}) = {math.ceil(y)}'    
    print(plb)
elif x == 0:
    y = x 
    plb = f'f({x:.2f}) = {math.ceil(y)}'     
    print(plb)
elif 0 < x <= 99:
    y = 3 * x ** 2 - (1 - x) ** 2
    plb = f'f({x:.2f}) = {math.ceil(y)}'  
    print(plb)
else:
    y = 2 * (x**3) - (x / (x+1)**(1/2))
    plb = f'f({x:.2f}) = {math.ceil(y)}'     
    print(plb)
    
