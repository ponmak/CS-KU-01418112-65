# 05 Fibonacci

def Fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        f1 = 1
        f2 = 1
        
        fibo = 0
        i = 0
        while i < num-2:
            fibo = f1 + f2
            f1 = f2
            f2 = fibo
            i += 1
            
        return fibo 
    
n = int(input("Enter n: "))
print("fibo({n}) = {f}".format (n = n, f = Fibonacci(n)))