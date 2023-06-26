'''
1) 각 자리의 숫자가 0~9로만 이루어짐
2) x, + 연산자를 넣어 결과적으로 만들 수 있는 가장 큰 수를 구하기
3) 모든 연산은 왼쪽에서 오른쪽으로 이루어짐
'''

'''
왼쪽, 오른쪽 수 중 0이나 1이 있으면 곱하는 거보다 더하는게 낫다
'''

from collections import deque 
import sys 
nums_str = sys.stdin.readline().rstrip()

nums = deque()
for num in nums_str :
    nums.append(int(num)) 

res = 0
while len(nums) != 1 :
    if (nums[0] == 0) or (nums[0] == 1) or (nums[1] == 0) or (nums[1] == 1) :
        res = (nums[0] + nums[1])
    else :
        res = (nums[0] * nums[1])
    
    nums.popleft()
    nums.popleft()
    nums.appendleft(res)

print(res)