'''
문자열 S에 있는 모든 숫자를 전부 같게 만들고 싶음

다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것
'''

import sys 
s = sys.stdin.readline().rstrip()

nums = [
    elem
    for elem in s 
]

s_0 = nums.copy()
s_1 = nums.copy()


# 문자열 s의 길이 
l = len(s)

# 문자열 S를 모두 0으로 바꾸는데 소요되는 횟수
# 문자열 S를 모두 1으로 바꾸는데 소요되는 횟수
cnt_0 = 0
cnt_1 = 0 

# 1) 모두 0으로 바꿀 때
while 1 :
    try : 
        idx = s_0.index('1')
    
    except : 
        break 
    
    else :
        s_0[idx] = '0'
        idx += 1
        while idx < l :
            if s_0[idx] == '0' :
                break 
            s_0[idx] = '0'
            idx += 1
        cnt_0 += 1


# 2) 모두 1으로 바꿀 때
while 1 :
    try : 
        idx = s_1.index('0')

    except : 
        break 
    
    else :
        s_1[idx] = '1'
        idx += 1
        while idx < l :
            if s_1[idx] == '1' :
                break 
            s_1[idx] = '1'
            idx += 1
        
        cnt_1 += 1

print(min(cnt_0, cnt_1))