def findIndex (a, n, key ): 
	for i in range(n-1, 0, -1): 
		if a[i] == key: 
			end = i+1
			break 
		else:
			end = -1
	print("Last index: ", end) 

num, k = input().split()
n = int(num)
key = int(k)
a = list(map(int,input().strip().split()))[:n]
findIndex(a, n, key) 

