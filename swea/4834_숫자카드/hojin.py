import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    
    numbers = list(input()) #이때 출력되는 리스트는 ['4', '9', '6', '7', '9'],['0', '8', '2', '7', '1'],['7', '7', '9', '7', '9', '4', '6', '5', '4', '3']

    count_num=0
    answer = 0

    for i in range(0,10):
        k = numbers.count(str(i))
        if k > count_num:
            count_num = k
            answer = int(i)
        elif k == count_num:  ## count가 같은 경우 numb라는 숫자 리스트를 만들어 오름차순으로 재정렬하였다.
            numb = list(map(int,numbers))
            numb.sort()
            answer = numb[-1]
        elif count_num > k:
            count_num = count_num
        

    print(f'#{tc} {answer} {count_num}')