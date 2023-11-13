def solution(A, B):
    answer = 0
    A_list = [i for i in A]
    count = 0

    if A != B:
        for j in A_list:
            k = A_list.pop()
            A_list.insert(0,k)
            count += 1
            check = ''.join(A_list)
            if check != B:
                answer = -1
            if check == B:
                answer = count
                break  
           
    elif A == B:
        answer = 0

    return answer

print(solution("hello","ohell"))
print(solution("apple","elppa"))
print(solution("atat","tata"))
print(solution("abc","abc"))