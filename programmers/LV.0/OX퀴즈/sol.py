def solution(quiz):
    answer = []
    for i in quiz:
        my_list = list(map(str, i.split())) 
        # list(map(str, i.split()))을 이용하여 ['3', '-', '4', '=', '-3'],['5', '+', '6', '=', '11'] 이런 식으로 리스트로 구분했다.
        # 식이 되기 위해선 숫자와 연산자가 번갈아 등장해야 하기때문에 my_list[1]은 무조건 연산자(+ or -)라는 점을 활용했다
        if my_list[1] == '-':
            result = int(my_list[0])-int(my_list[2])
            if result == int(my_list[4]):
                answer.append('O')
            elif result != int(my_list[4]):
                answer.append('X')
        elif my_list[1] == '+':
            result = int(my_list[0])+int(my_list[2])
            if result == int(my_list[4]):
                answer.append('O')
            elif result != int(my_list[4]):
                answer.append('X')
        
    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))




# eval이라는 문자열을 반아 수식으로 꼐산해주는 함수가 있다고 합니다
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]