# 03 หรม. และ ครน.

f_num = int(input('Enter the first number: '))
s_num = int(input('Enter the second number: '))
    
if f_num < s_num:
    f_num, s_num == s_num, f_num

FNUM = f_num
SNUM = s_num

next_num = -1
while True:
    next_num = f_num % s_num
    #print(f'(!) f_num : {f_num} | s_num : {s_num} | next_num : {next_num}')
    if next_num != 0:
        f_num = s_num
        s_num = next_num
        #print(f'(!) f_num : {f_num} | s_num : {s_num} | next_num : {next_num}')
    else:
        #print(f'(!) going out loop | f_num : {f_num} | s_num : {s_num} | next_num : {next_num}')
        break
           
print(f'  >> gcd({FNUM}, {SNUM}) = {s_num:>6}')    
print(f'  >> lcm({FNUM}, {SNUM}) = {FNUM * SNUM / s_num:>6.0f}')  
