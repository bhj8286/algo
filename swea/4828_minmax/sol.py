# # import sys 
# # sys.stdin = open('input.txt')

# # T =int(input())

# # for tc in range(1, T+1):
# #     N = int(input())

# #     numbers = list(map(int, input().split()))

# #     for i in range(len(numbers)-1, 0, -1):
# #         for j in range(i):
# #             left = numbers[j]
# #             right = numbers[j+1]

# #             if left > right:
# #                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# #     print(numbers[-1] - numbers[0])



import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 사용하진않지만 다른 언어에서는 사용해야 할 수도 있기때문에 변수로서 받아둔다. 파이썬에선 사용하지 않음

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



