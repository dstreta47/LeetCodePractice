arr= ['p','r','a','c','t','i','c','e',' ',
 'm','a','k','e','s',' ' , 'p','e','r','f','e','c','t']
# e,c,i,t,c,a,r,p 

def rev(arr, start,end):
        while(start<=end):
            arr[start],arr[end] = arr[end],arr[start]
            start+=1
            end-=1
        print("worked")
        return arr   

        


def reverseword(array, start=0, end=0):
    for end in range(len(array)-1):
        if array[end]== ' ':
            rev(array, start,  end-1)
            start= end+1
    rev(array, end+1,len(arr)-1)
    rev(array,0,len(arr)-1)
    

    #hacky 2 bit
    j=0
    for i in range(len(array)):

        while array[j] != ' ':
            j+=1

    ptr1=0
    ptr2= j-1
    for i in range(j-1):
        while ptr1<ptr2:
            temp= array[ptr1]
            array[ptr1]= array[ptr2]
            array[ptr2]= temp
            ptr1 +=1
            ptr2 -=1


reverseword(arr)
print(arr)
