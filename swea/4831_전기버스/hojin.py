import sys 
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    K, N, M = list(map(int,input().split()))
    charger = list(map(int,input().split()))
    