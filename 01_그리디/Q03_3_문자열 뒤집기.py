import sys 
s = sys.stdin.readline().rstrip()
l = len(s)

# count0 (1 -> 0)
# count1 (0 -> 1)
count0, count1 = 0, 0

# 첫 문자가 '0'이면, '1'로 바꿔줘야 하는 횟수 증가
if s[0] == '0' : 
    count1 += 1
# 첫 문자가 '1'이면, '0'로 바꿔줘야 하는 횟수 증가
else :
    count0 += 1

for i in range(1, l) :
    if s[i-1] != s[i] :
        if s[i] == '1' :
            count0 += 1
        else :
            count1 += 1

print(min(count1, count0))