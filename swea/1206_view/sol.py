# 내풀이
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    Buildings = int(input())
    height = list(map(int, input().split()))

    # 기준은 3번째 빌딩 
    View_floor = 0
    for i in range(2, Buildings-2):
        
        if height[i] > height[i+1] and height[i] > height[i+2] and height[i] > height[i-1] and height[i] > height[i-2]:
            View_floor += height[i] - max(height[i-2], height[i-1], height[i+1], height[i-2])
            
                
    print(f'#{tc} {View_floor}')

    # sum은 리스트의 값을 합해주는 것 sum을 쓸 거면 빈 리스트를 만들고 append해줘서 더해야함

# 강사님 풀이
# import sys
# sys.stdin = open('input.txt')

# T = 10

# for tc in range(1, T+1):
#     N = int(input())
#     buildings = list(map(int, input().split()))

#     total = 0

#     for i in range(N):
#         now = buildings[i]

#         # 현재 위치에 건물이 없다면 다음 건물로 이동
#         if now == 0:
#             continue
        
#         # 현재 위치에 건물이 있는경우
#         else:
#             dx = [-2, -1, 1, 2]

#             max_tall = 0

#             # 중심을 기준으로 네개의 건물중 가장 큰건물 고르기
#             for j in range(4):
#                 # i (now) : 현재위치 (기준점)
#                 # dx[j] : 기준 건물을 중심으로 좌우 인덱스
                
#                 comp = buildings[i+dx[j]]

#                 if max_tall < comp:
#                     max_tall = comp


#             # 나머지 네개의 건물보다 현재 건물의 높이가 크다면
#             # 조망권 확보!
#             if now > max_tall:
#                 view = now - max_tall
#                 total += view
    
#     print(f'{total}')