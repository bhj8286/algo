1
#     print(count)import sys
# sys.stdin = open('input.txt')

# T = int(input())

# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# temp = []

# count = 0

# for tc in range(1, T+1):
#     N,K = map(int, input().split())
#     # print(N, K)
#     for i in range(1,13):
#         for j in range(1<<N):
#             if i & (1<<j):
#                 temp.append(A[j])
            
#             if len(temp) == N & sum(temp) == K:
#                     count +=

#강사님 풀이
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = list(range(1, 13))
    N, K = list(map(int, input().split()))

    count = 0

    for i in range(1 << len(numbers)):
        temp = []
        for j in range(len(numbers)):
            if i & (1 << j):
                temp.append(numbers[j])

        if len(temp) == N and sum(temp) == K:
            count += 1

    print(count)