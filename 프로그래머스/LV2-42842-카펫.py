'''
가로 >= 세로

brown = (x+y)*2 - 4
yellow = x*y - brown
x + y = (brown + 4) / 2
x * y = yellow + brown

x >= y

24 24
x + y = 14
x * y = 48

for ix in range(3, brown/2):
    # y = brown/2 + 2 - x
    if ix * (brown/2 + 2 - ix) == yellow + brown:
        x = ix
        y = brown/2 + 2 - ix
        break

# 회고
방정식으로만 해서 풀수있을까 싶어서 시간낭비를 좀 했다. 
될꺼같은데? 싶으면 무조건 깊게파지 말고 '구조적으로' 가능한지 먼저 생각해보는 순간이 필요할것 같다

'''

def solution(brown, yellow):
    x = 0
    y = 0
    for ix in range(3, brown//2):
        # y = brown/2 + 2 - x
        if ix * (brown/2 + 2 - ix) == yellow + brown:
            x = int(ix)
            y = int(brown/2 + 2 - ix)
            break
    
    answer = [x, y]
    answer.sort(reverse=True)
    return answer