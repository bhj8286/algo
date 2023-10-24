def solution(s1, s2):
    answer = []
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                answer.append(s2[j])
            else:
                continue
    return len(answer)

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))
print(solution(["n", "omg"], ["m", "dot"]))