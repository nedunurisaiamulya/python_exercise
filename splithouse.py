N=int(input())
n=list(input())
n.append(0)
c=0
for i in range(N):
    if(n[i]==n[i+1]) and (n[i]=='H'):
        c=c+1
        break
    else:
        if n[i]==".":
            n[i]='B'
if c==0:
    print("YES")
    n=n[:-1:]
    print(''.join(n))
else:
    print("NO")
