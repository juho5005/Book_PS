import sys 
n = int(sys.stdin.readline()) # 1 <= N <= 100,000
fears = list(map(int, sys.stdin.readline().split()))

# sort by asc
fears.sort()

'''
공포도가 작은 사람들부터 그룹으로 만들기
'''

group = 0 

cnt = 0
for fear in fears :
    cnt += 1

    if cnt >= fear : 
        cnt = 0
        group += 1

print(group)