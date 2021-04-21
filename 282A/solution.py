n = int(input())
x = 0

for i in range(n):
    st = input()
    if st.count("++"):
        x = x + 1
    else:
        x = x - 1

print(x)