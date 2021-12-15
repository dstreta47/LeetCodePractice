
#hashtable
def twosum(num,target):
    dict1 = {}
    for i in range(len(num)):
        tofind = target - num[i]
        if tofind in dict1:
            return [dict1[tofind],i]
        else:
            dict1[num[i]] = i
            
#Two pointer
def twosum_2(nums,target):
    left = 0
    right = len(nums)-1
    while left<right:
        if nums[left] + nums[right] == target:
            return [left,right]
            left +=1
            right -=1
        elif  nums[left] < nums[right] :
            left+=1
        else:
            right -=1     


nums = [3,3]
target = 6
print(twosum_2(nums,target))
