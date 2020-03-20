n = int(input())
a = list(map(int,input().strip().split()))[:n] 
ans = 1
for i in a:
    ans = (ans*i%((pow(10, 9))+7))

print(ans)
