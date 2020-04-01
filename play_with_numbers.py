N, Q = map(int,input().split()
arr = list(map(int, input().strip().split()))[:N]
for i in range(int(Q)):
    ans =[]
    L, R = input().split()
    s = (L+R)/2
    ans.append(s)

print(*ans, end = "\n")
