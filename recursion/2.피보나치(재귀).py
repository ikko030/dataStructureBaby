#피보나치란 f(n)= f(n-1)+ f(n-2)
#단, f(1) = f(2) = 1

def fib(n):
    if n==1 or n==2:
        return 1
    
    else:
        return fib(n-1) +fib(n-2)
    

print(fib(4))

#재귀함수는 지수함수적으로 증가하기 때문애
#fib(100)을 하면 엄청난 시간이 걸린다.