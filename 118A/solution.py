s1 = input().lower()
s = ""
for i in range(s1.__len__()):
    if s1[i] not in "aeiouy":
        s = s + "." + s1[i]
print(s)