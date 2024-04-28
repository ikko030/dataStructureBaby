#a,b,c, 3개의 기둥이 있고, 기둥 a에 널이가 서로 다른 n개의 원반이 있다.
#n개의 원반을 기둥 b로 옮겨야 한다.
#단, 원반은 1개씩 옮길 수 있다.
#단, 큰 원반이 작은 원반 아래에 놓여 있어야 한다.

def hanoi(n, source, target, auxiliary):

    if n == 1:
        print(f"원반 1을 {source}-> {target}")
    else:
        hanoi(n-1, source, auxiliary, target)               # n-1개의 원반을 보조 기둥으로 옮김
        
        print(f"원반 {n}을 {source}-> {target}")            # 가장 큰 원반을 목표 기둥으로 옮김
        
        hanoi(n-1, auxiliary, target, source)               # 보조 기둥에 있는 n-1개의 원반을 목표 기둥으로 옮김



hanoi(3, 'A', 'C', 'B')


'''
와 이해가 안가서 3시간 동안 잡고 있었당...

hanoi(3,A,B,C)
=>hanoi(2,A,B,C)  -> hanoi(1,A,C,B) -> 원반2을 A->B 출력 -> hanoi(1,C,B,A)
=>원반3을 A->B출력
=>hanoi(2,B,C,A) -> hanoi(1,B,A,C) -> 원반1을 B->A 출력  -> hanoi(1,A,C,B)
'''

