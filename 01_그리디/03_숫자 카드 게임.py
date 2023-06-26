import sys 
n, m = tuple(map(int, sys.stdin.readline().split()))

board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

max_num = float('-inf')

for i in range(n) :
    min_num = float('inf')
    
    for j in range(m) :
        min_num = min(min_num, board[i][j])
    
    # 각 행의 최솟값중 최댓값을 찾아 갱신
    max_num = max(max_num, min_num)

print(max_num)