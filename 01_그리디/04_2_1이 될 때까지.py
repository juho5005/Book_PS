# 어떠한 수 N이 1일 될 때까지 두 과정을 반복적으로 실행
# 두 번째 연산은 N이 K로 나누어떨어질 때만 선택 가능

import sys 
n, k = tuple(map(int, sys.stdin.readline().split()))
# 2 <= n, k <= 100,000
# O(1), O(logN), O(N), O(NlogN)

'''
만약 N의 값이 커지게 된다면 앞선 코드로는 시간초과가 발생하게 됨
N이 나눠지는 숫자까지 빼는 과정에서 시간을 줄이는 방법을 찾는 것이 좋음
'''

cnt = 0
while 1 :
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기 
    target = (n//k) * k 
    cnt += (n - target)
    n = target 

    # 만약 N이 K보다 작을 때(더 이상 나눌 수 없을 때 남은 수를 빼주고반복문 종료)
    if n < k : 
        cnt += (n-1)
        break 
    
    # n을 k로 나누어준 값으로 바꾸고 
    # 횟수를 1회 늘려줌
    n //= k 
    cnt += 1

print(cnt)