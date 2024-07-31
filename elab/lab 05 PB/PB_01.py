# 01 พิมพ์หลักของเลขจำนวนเต็มบวก

num = int(input())
temp_num = 0

if num <= 0:
    print('ERROR')
else:
    while True:
        print(num % 10)
        num = num // 10
        if num <= 0:
            break

        
        
        
