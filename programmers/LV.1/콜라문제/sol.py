# 처음 생각: 내가 줘야되는 콜라병수 :a, 받는 콜라병수: 준 콜라병수/a * b라고 생각
def solution(a, b, n):
    answer = 0
    bottles = 0
    while n >= a:
        x, y = divmod(n,a)
        answer += x * b # 이 부분에선 b를 잘 곱해줬다
        bottles = (x * b) + y # 이 부분 역시 내가 받는 콜라병인 걸 간과하여 bottles = x + y로 설정해버려 처음에 오류가 났다. b를 곱해주니 통과
        n = bottles
    return answer


print(solution(2, 1, 20))
print(solution(3, 1, 20))
