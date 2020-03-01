x, y = input().split() 
r = int(x)
c = int(y)
matrix = []
for i in range(c):
    x = list(map(float, input("Enter a multiple value:").split()))[:r]
    matrix.append(x)
t_matrix = zip(*matrix) 
for row in t_matrix: 
    num = 0
    for i in row:
        num = num+i
    avg = num/len(row)
    print(avg)

