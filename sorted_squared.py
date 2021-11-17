def sorted_squared(list1):
    res = []
    l =0
    r = len(list1)-1
    while(l<r):
        if abs(list1[l]) > abs(list1[r]):
            res.append(list1[l]*list1[l])
            l+=1
        else:
            res.append(list1[r]*list1[r])   
            r-=1  



list1 = [-7,-5,-4,3,6,8,9]
sorted_squared(list1)
