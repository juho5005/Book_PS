import sys 
s = sys.stdin.readline().rstrip()
l = len(s)

# 1) 0 -> 1로 바꾸는 경우
i = 0 
cnt1 = 0

while i < l : 
    if s[i] == '0' :
        i += 1
        while i<l and s[i] == '0' :
            i += 1
        cnt1 += 1
    else :
        i += 1

# 2) 1 -> 0로 바꾸는 경우
j = 0
cnt2 = 0

while j < l :
    if s[j] == '1' :
        j += 1
        while j<l and s[j] == '1' :
            j += 1
        cnt2 += 1
    else :
        j += 1

print(min(cnt1, cnt2))