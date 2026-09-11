# https://school.programmers.co.kr/learn/courses/30/lessons/42839

def dfs(N, CART, visited, RSLT):
    # if len(CART) == len(N):
    #     print(f"cart: {CART}")
    #     rslt = ''.join(map(str, CART))
    #     RSLT.append(rslt)
    #     return
    
    for i in range(len(N)):
        if visited[i]:
            continue
            
        visited[i] = True
        CART.append(N[i])
        
        # 넣으면 바로바로 결과에 기록 (따로 CART 다 찼을때 기록하고 return하는 코드 필요X)
        rslt = ''.join(map(str, CART))
        RSLT.append(rslt)
        
        dfs(N, CART, visited, RSLT)

        visited[i] = False
        CART.pop()

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    
    return prime
    

def solution(numbers):
    answer = 0
    
    cart = []
    result = []
    visited = [False]*len(numbers)
    dfs(numbers, cart, visited, result)
    
    answ = set()
    for s in result:
        s = int(s)
        if is_prime(s) and s != 0:
            answ.add(s)
    
    return len(answ)

'''
## 문제조건
[ 숫자들로 만들 수 있는 소수 개수 ]
    - 숫자 이어붙이기 가능

    * 숫자개수: 1~7
    * 숫자: 0~9

## 접근흐름
    - 최악 복잡도(완탐):
        * 모든경우의수 = 7! * 2^7 = 64만
        * 소수인지판별 = 64만 * 7 = 400만
    - [예외] 011이나 11이나 같은 숫자 취급
    - [예외] 끝자리가 짝수나 5인 경우 소수 아님 (2,4,6,8,0,5)
        - [예외] 한자리 2, 5는 소수!
        
    <문제> 순열로 모든 케이스 만드는 법?
    : DFS
    
    <계획>
    1: dfs로 모든 순열 만들어 set에 넣기(중복제거) -- O(2^7 * 7!)
    2: 각각 소수인지 판별 (*n)
    3: 개수 리턴
    

'''