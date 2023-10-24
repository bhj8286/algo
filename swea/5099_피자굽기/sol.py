import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 화덕의 갯수: M: 피자의 갯수
    N, M = list(map(int, input().split()))
    c = list(map(int, input().split()))
    Queue = [] 
    for i in range(1, N+1):
        Queue.append(i)
        for j in range(M):
            if c[i]//2 == 0:
                Queue.pop[i]
            elif c[i]//2 > 0:
            
            #pop(0), append(0)의 정확한 의미, 0이라는 값을 빼고싶을땐 어떻게 해야하는지?
            