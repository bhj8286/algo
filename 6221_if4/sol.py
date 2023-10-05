import sys
sys.stdin = open('input.txt', encoding='utf-8')

man1 = input()
man2 = input()

rcp = ['가위', '바위', '보']

man1_idx = rcp.index(man1)
man2_idx = rcp.index(man2)

result = man1_idx - man2_idx

if result == 0:
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man{result} Win!')
else:
    if result == -1:
        print('result : Man2 Win!')
    else:
        print('result : Man1 win!')