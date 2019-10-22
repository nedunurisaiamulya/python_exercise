def unique(list1): 
  
    unique_list = [] 
      
    for x in list1: 
        if x not in unique_list: 
            unique_list.append(x) 
    print (unique_list) 
    print(unique_list[::-1])
      
      
num=int(input())
list1 = []
for i in range(0,num):
    x = int(input()) 
    list1.append(x) 
unique(list1) 
