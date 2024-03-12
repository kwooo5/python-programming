def fib(n):
    if n <= 1:
        return n 
    else:
        return fib(n-1) + fib(n-2)
n = 10
print ('fibonacci sequence:')
for i in range(n):
    print(fib(i))
    
