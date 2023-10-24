import sys
from pprint import pprint
sys.stdin = open('input.txt')
import random


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [[0 for _ in range(N)]for _ in range(N)]
    # print(board)
    Min_number = 10000000
    numbers = [] 
    for i in range(N):
        number = list(map(int,input().split()))
        numbers.append(number)  #numbers라는 빈 리스트에 number을 받는 것이 numbers라는 2차원 배열을 만드는 것
        Min_sum = 0
        sample_list = random.sample(numbers[i][i],1)

        
        
        
        
        
