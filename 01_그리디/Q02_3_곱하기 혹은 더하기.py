'''
1) 각 자리의 숫자가 0~9로만 이루어짐
2) x, + 연산자를 넣어 결과적으로 만들 수 있는 가장 큰 수를 구하기
3) 모든 연산은 왼쪽에서 오른쪽으로 이루어짐
'''

'''
왼쪽, 오른쪽 수 중 0이나 1이 있으면 곱하는 거보다 더하는게 낫다
'''

import sys 
nums_str = sys.stdin.readline().rstrip()

# 문자열의 길이
l = len(nums_str)

# 초기값 설정
res = int(nums_str[0])

for i in range(1, l) :
    if (res <= 1) or (int(nums_str[i]) <= 1) :
        res += int(nums_str[i])
    else :
        res *= int(nums_str[i])
        
print(res)