# 어떠한 수 N이 1일 될 때까지 두 과정을 반복적으로 실행
# 두 번째 연산은 N이 K로 나누어떨어질 때만 선택 가능

import sys 
n, k = tuple(map(int, sys.stdin.readline().split()))
# 2 <= n, k <= 100,000
# O(1), O(logN), O(N), O(NlogN)

cnt = 0
while n != 1 : 
    # 1번 과정이 우선순위를 가짐
    if n%k != 0 :
        n -= 1
    
    else :
        n //= k 
    
    cnt += 1

print(cnt)