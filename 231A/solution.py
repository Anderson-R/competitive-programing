n = int(input())
s = 0

for i in range(n):
    line = input()
    a = line.split(' ')
    b = 0
    for j in a:
        b = b + int(j)
    if b >= 2:
        s = s + 1

print(s)    