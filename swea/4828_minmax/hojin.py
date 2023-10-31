import sys
sys.stdin = open('input.txt')

T= int(input()) 

for tc in range(1, T+1):
    N = int(input())
    my_list = list(map(int, input().split()))
    my_list.sort()
    answer = my_list[-1]-my_list[0]

    print(f'#{tc} {answer}')