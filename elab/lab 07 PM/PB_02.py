# 02 จุดในสี่เหลี่ยม

print('Upper left corner coordinate:')

r_x1 = float(input('  << x axis: '))
r_y1 = float(input('  << y axis: '))
r_es = float(input('  << Eastern: '))
r_st = float(input('  << Southern: '))

print('Enter a coordinate:')

x = float(input('  << x axis: '))
y = float(input('  << y axis: '))

if y < r_y1 - r_st or x > r_x1 + r_es or r_x1 > x  or r_y1 < y:
    print(f'>>> ({x:.2f}, {y:.2f}) is not inside the rectangle.')
else:
    print(f'>>> ({x:.2f}, {y:.2f}) is inside the rectangle.')



