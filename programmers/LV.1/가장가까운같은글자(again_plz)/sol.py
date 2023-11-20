## 내 풀이
def solution(s):
    answer = []
    for x,y in enumerate(list(s)):
        for j in range(x-1,0,-1):
            k = s[j]
            if y == k:
                answer.append(x-j)
                break
        else:
            answer.append(-1)

    return answer

print(solution("banana"))
print(solution("foobar"))

# 비슷한 풀이   # 딕셔너리 추가를 활용하여 글자의 마지막 위치를 저장해주는 좋은 방법인 것같다.
def solution(s):
    answer = []

    word_dict = {}

    for idx, word in enumerate(list(s)):
        if word not in word_dict:
            answer.append(-1)
            word_dict[word] = idx
        else:
            answer.append(idx - word_dict[word])
            word_dict[word] = idx
    return answer
print(solution("banana"))
print(solution("foobar"))
