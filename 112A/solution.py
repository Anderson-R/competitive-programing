s1 = input().lower()
s2 = input().lower()
s = 0

for i in range(s1.__len__()):
    if s1[i] < s2[i]:
        s = -1
        break
    elif s1[i] > s2[i]:
        s = 1
        break

print(s)