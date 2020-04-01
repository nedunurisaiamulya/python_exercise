from itertools import permutations
T = int(input())
for i in range(T):
    s1, s2 = input().strip().split()
    permutation = [''.join(p) for p in permutations(s1)]
    perm = str(permutation)
    if s2 in perm:
        print("YES")
    else:
        print("NO")

