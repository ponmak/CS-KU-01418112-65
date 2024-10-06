# 05 ผลบวกของเลข Fibonacci 

def fibo(n:int ) -> int :
    fibo = [1,1]
    fibo_sum = 0
    i = 0
    while i < n:
        fibo_sum = fibo[i] + fibo[i+1] # Is this DP ???? IDK 
        fibo.append(fibo_sum)
        i += 1
    #print(fibo)
    return fibo[i]

num = int(input())
e_or_o = input()

if e_or_o in ['e','E'] and num >= 0:
    print(sum([fibo(i) for i in range(num+1) if i % 2 == 0]))
elif e_or_o in ['o', 'O'] and num > 0:
    print(sum([fibo(i) for i in range(num+1) if i % 2 != 0]))
else:
    print("ERROR")
