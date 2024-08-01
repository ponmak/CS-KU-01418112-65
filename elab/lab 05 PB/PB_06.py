# 06 กฎของเก้า

number = int(input())
digit_sum_num = 0

while True:
    digit_sum_num += number % 10
    number //=  10 
    if number <= 0:
        break
    else:
        pass

if digit_sum_num % 9 != 0:
    print(f'No {digit_sum_num % 9}')
else:
    print(f'Yes {digit_sum_num}')
