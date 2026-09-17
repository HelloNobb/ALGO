def solution(triangle):
    answer = 0
    
    for i in range(len(triangle)):
        if i == 0:
            continue
            
        for j in range(len(triangle[i])):
            if j == 0:
                MAX = triangle[i-1][0]
            elif j == len(triangle[i])-1:
                MAX = triangle[i-1][-1]
            else:
                MAX = max(triangle[i-1][j-1], triangle[i-1][j])
            
            triangle[i][j] += MAX
        
        if i == len(triangle)-1:
            answer = max(triangle[i])
    
    return answer


'''
## 조건
    [ 위->아래 이진트리 내려가서 바닥 도착할때까지 값의 합 최대인 경우 구하기 ]

    * 트리 높이: 1~500
    * 값: 0~9999
    
## 접근
    -bfs를 생각했으나 경로에서 DP 문제라는걸 알아버림
    
    0: 한칸씩내려가며, 전 인덱스(좌/우) 중 큰값 + 자기값 으로 대체
    1: 마지막줄 중 가장 큰 값 return
'''