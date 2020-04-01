N = int(input())
arr = []
for i in range(N):
    I = input()
    L = I.split()
    if L[0]=='insert':
        arr.insert(int(L[1]),int(L[2]))
    elif L[0] == 'print':
        print(arr)
    elif L[0] == 'remove':
        arr.remove(int(L[1]))
    elif L[0] == 'append':
        arr.append(int(L[1]))
    elif L[0] == 'sort':
        arr.sort()
    elif L[0] == 'pop':
        arr.pop()
    elif L[0] == 'reverse':
        arr.reverse()


