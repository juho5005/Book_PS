''''
배열의 크기 N
숫자가 더해지는 횟수 M
배열의 특정한 인덱스 (번호)에 해당하는 수가 연속해서 K번을 초과해서 더할 순 없음
'''

import sys 
n, m, k = tuple(map(int, sys.stdin.readline().split()))

nums = list(map(int, sys.stdin.readline().split()))

# 내림차순 정렬
nums.sort(reverse=True)

first_max = nums[0]
second_max = nums[1]

# 큰 수의 법칙에 따른 결과
res = 0

k_instead = k 
while m :
    if k_instead == 0 :
        res += second_max 
        k_instead = k
    else :
        res += first_max 
        k_instead -= 1
    m -= 1
    
print(res)