# 처음 생각: 3C2, 5C3을 하기 위해 코드를 아래와 같이 작성함
def solution(balls, share):
    answer = 0
    ball = 1
    methods = 1
    for b in range(share,balls+1):
        ball *= b
    for m in range(1,share+1):
        methods *= m
    answer = int(ball / methods)
    return answer

print(solution(3, 2))
print(solution(5, 3))

