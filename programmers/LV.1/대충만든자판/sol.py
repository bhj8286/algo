def solution(keymap, targets):
    answer = []
    for i in targets:
        result = []  # keymap의 단어가 바뀔 때마다 리스트가 초기화되게끔 result는 여기에
        for j in i:
            total = []  # targets의 단어 중 알파벳이 keymap의 단어들에서 모두 검증하기 위해 위치는 여기에
            a = -1     # 없는 경우 -1을 넣기위해 a=-1로 설정
            for k in keymap:
                if j in k:
                    total.append(k.index(j)+1)
                    a = min(total)
            result.append(a)
        if -1 not in result: ## keymap : ["BC"], targets : ["AC","BC"], 기댓값 : [-1,3] 인 경우 
            answer.append(sum(result)) # result의 합이 1이 나와서 결과값이 [1,3]이 나온다, 그런 경우를 방지에 result에 -1있으면 그냥 바로 -1 출력
        elif -1 in result:
            answer.append(-1)
   
    return answer

print(solution(["ABACD", "BCEFD"],     ["ABCD","AABB"]))
print(solution(["AA"],  ["B"]))
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))







