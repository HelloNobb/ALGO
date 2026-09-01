'''
각 자리마다 이전 행에서 가장 큰 수(자기자리 제외)를 더하면서 쭉쭉 내려감

# solution
for i in range(1, len(land)):
    for j in range(0, len(row)):
        for k in range(0, len(row)):       # 이전 항 조회
            if k != j:      # 다른 열일 경우
                land[i][j] = land[i-1][k]

# review
처음에 잘못된 방향으로 생각해서 시간을 한참 날렸다.
로직을 떠올렸을 때, 충분히 반례를 고민한 후 코드를 짜야겠다

'''

def solution(land):
    answer = 0

    for i in range(1, len(land)):
        for j in range(4):
            prev_max = 0
            for k in range(4):       # 이전 항 조회
                if k != j:      # 다른 열일 경우
                    if land[i-1][k] > prev_max:
                        prev_max = land[i-1][k]
            land[i][j] += prev_max
    answer = max(land[-1])
    return answer