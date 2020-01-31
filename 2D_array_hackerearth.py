R, C = input().split()
R = int(R)
C = int(C)
array = []
for i in range(R):
    ar = list(map(int, input().rstrip().split()))[:C]
    array.append(ar)
REV = [[array[j][i] for j in range(len(array))] for i in range(len(array[0]))]

for r in REV:
    for c in r:
        print(c,end = " ")
    print()
