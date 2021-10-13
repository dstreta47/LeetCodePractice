# Sub array divide into two such that left is greater sum thn right

def car(nums):  
    counts  = {}
    reducedPriority = 1 

    for i in nums:
        counts[i] = i

    for index,value in counts.items():
        reducedPriority = reducedPriority +1
        counts[index] =  reducedPriority

    for index,value in counts.items():
        nums[index] = counts[nums[index]]

    return nums    






print(car([1,3,7,3]))
