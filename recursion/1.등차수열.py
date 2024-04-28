#공차가 5인 등차수열
#초항은 1
def seq(n):
    if n==1:
        return 1
    
    else:
        return seq(n-1) + 5
    

print(seq(3))