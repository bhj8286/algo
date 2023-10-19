#내풀이
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    dump_num = int(input())
    box_height = list(map(int, input().split()))


    count = 0
    for idx, value  in enumerate(box_height):
        for idx in range(0, 99):
            if box_height[idx] < box_height[idx+1] :
                box_height[idx] +=1
                box_height[idx+1] -= 1 
                count += 1
            elif box_height[idx] > box_height[idx+1]:
                box_height[idx] -=1
                box_height[idx+1] += 1 
                count += 1
            else:
                if count == dump_num: break
        result = max(box_height) - min(box_height)

    print(f'#{tc} {result}')
            


##강사님 풀이
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))

    # while dump > 0:
    #   dump -= 1
    for i in range(dump):
        # 최대높이
        top_box = boxes[0]
        top_box_idx = 0
        # 최소높이
        down_box = boxes[0]
        down_box_idx = 0

        # 최대와 최소 높이 찾기
        for i in range(len(boxes)):
            if top_box < boxes[i]:
                top_box = boxes[i]
                top_box_idx = i

            if down_box > boxes[i]:
                down_box = boxes[i]
                down_box_idx = i

        # top_box = max(boxes)
        # down_box = min(boxes)

        # 평탄화
        boxes[top_box_idx] -= 1
        boxes[down_box_idx] += 1

        # 전체 평탄화 횟수 전에 평탄화가 완료된 경우
        if boxes[top_box_idx] - boxes[down_box_idx] < 1:
            break

    result = max(boxes) - min(boxes)

    print(f'{result}')

    
