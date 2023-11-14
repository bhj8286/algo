def solution(before, after):
    answer = 0
    before_list = []
    after_list = []
    for i in before:
        before_list.append(i)
        before_list.sort()
    for j in after:
        after_list.append(j)
        after_list.sort()

    if before_list == after_list:
        answer = 1
    elif before_list != after_list:
        answer = 0

    return answer

print(solution("olleh", "hello"))
print(solution("allpe", "apple"))


## 내가 구현하고자했던 이상적인 코드 형태 (참고: 리스트.sort() 는 본체의 리스트를 정렬해서 변환하는 것이고,
# sorted(리스트) 는 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환하는 것입니다. 문자열은 sort가 아닌 sorted를 사용해야 합니다)

# def solution(before, after):
#     before=sorted(before)
#     after=sorted(after) --> 이걸 몰라서 리스트에 넣고 정렬하는 번거로운 과정을 거침
#     if before==after:
#         return 1
#     else:
#         return 0


## 한줄 코드가 무조건적으로 좋은 것은 아니지만 멋져보임
# # 쿨남 코드
#  
# def solution(before, after):
#     return 1 if sorted(before)==sorted(after) else 0