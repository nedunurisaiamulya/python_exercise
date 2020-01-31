N = input()
n = int(N)
my_dict = {}
for i in range(n):
    key, value = input().split(" ")
    my_dict[key]=value

Q = input()
q = int(Q)
q_query = []
for i in range(q):
    x = input()
    X = my_dict[x]
    q_query.append(X)

print(*q_query, sep="\n")



