# 첫 시도 풀이: error가 모두 runtime 초과 
def solution(N, stages):
    answer = []
    st_num = list(range(1,N+1))
    fail = [] 
    for i in range(1,N+1):
        challenger = []
        for j in stages:
            if j >= i:
                challenger.append(j)
        fail.append(stages.count(i)/len(challenger))
    percentage = dict(zip(st_num, fail))
    fail = sorted(fail,reverse=True)
    for l in fail:
        for k,v in percentage.items():  
            if v == l:
                answer.append(k)
                percentage[k] = 501
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))

# 내 풀이 수정 버전 코드: 런타임 줄이기 위해
def solution(N, stages):
    answer = []
    fail = {}

    # for i in range(1, N + 1):: 1부터 N까지의 스테이지를 대상으로 반복
    # challenger = [j for j in stages if j >= i]: 현재 스테이지 i보다 크거나 같은 플레이어들을 stages 리스트에서 모아서 challenger 리스트에 저장
    for i in range(1, N + 1):
        challenger = [j for j in stages if j >= i] # 1. list comprehension 사용
        if len(challenger) == 0: # 2. 실패율을 계산할 때 ZeroDivisionError를 방지하기 위해 len(challenger)가 0일 경우에 대한 처리 추가
            fail[i] = 0
        else:
            fail[i] = stages.count(i) / len(challenger)
    
    #fail.items()는 fail 딕셔너리의 키-값 쌍을 (키, 값)의 튜플 형태로 반환.
    # key=lambda x: x[1]는 각 튜플에서 두 번째 원소(즉, 실패율)를 기준으로 정렬하도록 지정. 여기서 x[1]은 두 번째 원소를 나타냄
    # reverse=True는 내림차순으로 정렬하기 위해
    sorted_fail = sorted(fail.items(), key=lambda x: x[1], reverse=True) # 3.정렬 시에 sorted 함수의 key 매개변수를 사용하여 값을 기준으로 정렬

    for k, v in sorted_fail:
        answer.append(k) # 4. 정렬된 딕셔너리의 키를 answer 리스트에 추가

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
