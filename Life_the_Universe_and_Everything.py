from itertools import count
arr =[]
for i in count(0):
    try:
        numb = int(input())
    except EOFError:
        break
    arr.append(numb)

for i in arr:
    if i == 42:
        break
    else:
        print(i)
