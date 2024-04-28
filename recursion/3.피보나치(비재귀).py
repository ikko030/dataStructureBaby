def fib_fast(n):
    # 리스트 f를 크기 n+1로 초기화
    f = [0] * (n + 1)       # n=3이면, f = [0,0,0,0]

    if n == 1 or n == 2:
        return 1

    # 초기 피보나치 값 설정
    f[1], f[2] = 1, 1

    # f[3]부터 f[n]까지 피보나치 수 계산
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    
    return f[n]



print(fib_fast(10))  
