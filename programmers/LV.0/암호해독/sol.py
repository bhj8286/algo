def solution(cipher, code):
    answer = ""
    for i in range(len(cipher)):
        k = i + 1 
        if k % code == 0:
            answer += cipher[i]
        else: 
            continue
    return answer

print(solution("dfjardstddetckdaccccdegk", 4))
print(solution("pfqallllabwaoclk", 2))
