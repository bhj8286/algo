def solution(id_pw, db):
    answer = ''
    for x, y in db:
        if x == id_pw[0]:  ##아이디가 통과했을 때
            if y == id_pw[1]: # 비밀번호까지 똑같다면 로그인 성공 그러나 이후에도 for문이 반복된다면 마지막 결과가 도출 되므로 break를 걸어준다
                answer = 'login'
                break
            elif y != id_pw[1]:
                answer = 'wrong pw'
            break # 아이디가 통과한 경우가 있다면 비밀번호를 판별하면 되므로 break를 걸어준다
        else:  ## 아이디조차 통과못했을 때
            answer = 'fail'
    return answer


print(solution(["meosseugi", "1234"],[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
print(solution(["rabbit04", "98761"], [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))