# import sys 
# sys.stdin = open('input.txt')

# T =int(input())

# for tc in range(1, T+1):
#     N = int(input())

#     numbers = list(map(int, input().split()))

#     for i in range(len(numbers)-1, 0, -1):
#         for j in range(i):
#             left = numbers[j]
#             right = numbers[j+1]

#             if left > right:
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

#     print(numbers[-1] - numbers[0])



import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    numbers = list(map(int, input().split()))

    min_number = 1000000000
    # min_number = numbers[0]
    max_number = 0
    # max_number = numbers[0]

    for number in numbers:
        if min_number > number:
            min_number = number

        if max_number < number:
            max_number = number

    result = max_number - min_number

    print(f'#{tc} {result}')
