n = input()
N = int(n)
A = list(map(int, input().strip().split()))[:N]
B = list(map(int, input().strip().split()))[:N]
Arr =[]
for i in range(N):
    a = A[i]
    b = B[i]
    c = a+b
    Arr.append(c)

print(*Arr, sep=" ")

