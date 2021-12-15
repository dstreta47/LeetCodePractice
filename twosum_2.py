
def twosum(num,target):
    dict1 = {}
    for i in range(len(num)):
        tofind = target - num[i]
        if tofind in dict1:
            return [dict1[tofind],i]
        else:
            dict1[num[i]] = i

nums = [3,3]
target = 6
print(twosum(nums,target))
