'''
값을 저장하며 배열 순회
자신이 받을 수 있는 값(left, right) 중 항상 더 큰값을 선택해 자신의 값에 더함
이걸 계속 반복..
leaf중 가장 큰 값 리턴

# psuedo code
for i in range(1, len(triangle)):       # 두번째 줄부터 순회 시작
    for j in range(len(triangle[i])):
        if j == 0:                      # 왼쪽 끝
            triangle[i][j] += triangle[i-1][j]
        elif j == len(triangle[i]) - 1: # 오른쪽 끝
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

return max(triangle[-1])

'''

def solution(triangle):
    for i in range(1, len(triangle)):       # 두번째 줄부터 순회 시작
        for j in range(len(triangle[i])):
            if j == 0:                      # 왼쪽 끝
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1: # 오른쪽 끝
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return max(triangle[-1])

