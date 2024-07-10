# ผลรวมเศษส่วน

#First fraction
print('First fraction:')
f_numerator = int(input('>>Enter a numerator a: '))
f_denominator = int(input('>>Enter a denominator b: '))

#Second fraction
print('Second fraction:')
s_numerator = int(input('>>Enter a numerator c: '))
s_denominator = int(input('>>Enter a denominator d: '))

#Sum all fraction
denominator = s_denominator * f_denominator
numerator = (f_numerator * s_denominator) + (s_numerator * f_denominator)

# using f string for easy printing
print(f'Summation of the two fractions is {numerator} / {denominator}')

