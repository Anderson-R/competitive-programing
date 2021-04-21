n = int(input())
x = []
y = []
z = []

for i in range(n):
    a = input()
    b = a.split(' ')
    x.append(int(b[0]))
    y.append(int(b[1]))
    z.append(int(b[2]))

if sum(x) != 0:
    print("NO")
    exit()
if sum(y) != 0:
    print("NO")
    exit()
if sum(z) != 0:
    print("NO")
    exit()

print("YES")
