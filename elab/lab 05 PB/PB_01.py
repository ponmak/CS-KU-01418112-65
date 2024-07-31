# 01 พิมพ์หลักของเลขจำนวนเต็มบวก

num = int(input())

if num <= 0:
    print('ERROR')
else:
    i = num % 10
    counter = 0
    while counter < i:
        num = str(num)
        print(num[(i - counter) * -1])
        counter += 1
        
