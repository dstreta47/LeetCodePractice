def two_sum(list1,target):
    dict1= {}
    for i in range(len(list1)):
        to_seek = target - list1[i]
        if to_seek in dict1:
            return [to_seek,list1[i]]
        else:
            dict1[i] = True   
            

    print(dict1)        
        
    
 #O(nlogn)   
def two_sum_bin(list1,target):
    i = 0
    j = len(list1)-1
    list1 = sorted(list1)
    while(len(list1)-1):
        if list1[i]+list1[j] == target:
            return [list1[i],list1[j]]
        elif list1[i]+list1[j] < target: 
            i+=1
        else:
            j-=1  


list1 = [3,5,-4,8,11,1,-1,6]
target = 90
print(two_sum(list1,target))
#ans = [11,-1]
