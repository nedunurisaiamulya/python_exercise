def t(arr, n):
  list.sort()
  x = []
  i = 0
  while (i< n/ 2 ) :
   x.append(arr[i]) 
   i = i + 1
        
  j = n - 1
  while j >= n / 2 : 
   x.append(arr[j]) 
   j = j - 1
  print(x)

num=int(input())
list = []
for i in range(num):
  x =int(input())
  list.append(x)
print(list)

t(list, num)

