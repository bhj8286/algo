import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = list(range(1, 13))
    N, K = list(map(int, input().split()))

