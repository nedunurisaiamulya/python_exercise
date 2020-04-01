word = input()
sm = 'zoo'
tz = word.count('z')
to = word.count('o')
if tz*2 == to:
    if sm in word:
        print('Yes')
else:
    print('No')
