def conject_it(n):
    if n == 1:
        return "YES"
    elif n < 1:
        return "NO"
    elif (n%2 == 0):
        return conject_it(n//2)
    else:
        return conject_it((3*n)+1)

T = input()
for i in range(int(T)):
    n = int(input())
    print(conject_it(n))
