# import sys
# sys.stdin = open('input.txt')

# n = list(map(int, input().split()))

# print(n)

# a = [1, 2, 3, 4, 5, 6]
# counter = 0

# for idx, value in enumerate(a):
#     if idx >= 2:
#         counter += 1

# print(counter)

# a = [1, 2, 3, 4, 5, 6]
# counter = 0

# for idx in a:
#     if idx >= 2:
#         counter += 1

# print(counter)


# 질문할 것: idx의 정의, n번째를 나타나는 것이 idx인 줄 알았는데 enumerate를 하지 않으면 idx는 key, value중 value에 해당하는건지?
# 질문할 것: swea의 문제를 풀때 T,tc는 자체적으로 정의된 변수로 보고 따로 정의할 필요없이 정의되어 졌다고 보는것인지?


a = 3
b = 4
print(divmod(a,b))  # -> 몫,나머지를 출력한다 출력결과 (0, 3)

c = [1 , 'a', 2, 'k']
# c.pop() 마지막 번째 값인 k를 삭제한 리스트를 출력해준다
# c.pop(0) 0번째 숫자인 1을 삭제한 리스트를 출력해준다 
# print(c.pop()) -> 뭘 삭제했는지를 보여준다.

a = {
       'name'  : '호진',
}
a[ 'phone' ] = '010- 8286-5167'
print(a['phone'])

# input이란 데이터를 한 줄 받아오는 것 