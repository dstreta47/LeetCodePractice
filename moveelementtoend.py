def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j]= temp
    return arr 


def movetoend(arr,s,res):
    i = 0
    j=len(arr)-1
    while(i<=j):
        if arr[i] ==s and arr[j]!=s:
            arr = swap(arr,i,j)
        if arr[j]==s:
            j-=1

        i+=1   
    return arr    


arr = [4,1,3,2,2,8,6,3]
s = 2
res = []
print(movetoend(arr,s,res))
