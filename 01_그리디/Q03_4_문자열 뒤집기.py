import sys 
s = sys.stdin.readline().rstrip()
l = len(s)

# 스택 생성
stack = []

# 첫 번째 문자열의 원소를 스택에 넣어준다.
stack.append(s[0])

for i in range(1, l) :
    if stack[-1] != s[i] : # 스택의 마지막 원소가 s[i]와 다르면 스택에 append
        stack.append(s[i])

# count0 (1 -> 0 바꾸는데 필요한 횟수)
# count1 (0 -> 1 바꾸는데 필요한 횟수)
count0 = stack.count('1')
count1 = stack.count('0')

print(min(count0, count1))