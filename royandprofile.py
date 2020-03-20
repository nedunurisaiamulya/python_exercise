L = int(input())
N = int(input())
for i in range(N):
    W, H = map(int, input().strip().split())
    if (W < L or H < L):
        print("UPLOAD ANOTHER")
    elif(W >= L or H >=L):
        if(W == H):
            print("ACCEPTED")
        else:
            print("CROP IT")
