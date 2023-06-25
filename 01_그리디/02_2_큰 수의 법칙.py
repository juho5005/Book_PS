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

'''
만약 m이 커지게 된다면 앞선 코드 방식으로는 시간 복잡도가 O(m)이므로 시간 초과가 발생
그러므로 시간 초과를 줄이는 방법을 고안해야함 
'''

# 가장 큰 수가 더해지는 횟수
a = (m // (k+1)) * k + (m % (k+1))

# 두 번째로 큰 수가 더해지는 횟수
b = m - a

res = (a * first_max) + (b * second_max)

print(res)