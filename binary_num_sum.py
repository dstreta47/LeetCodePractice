#program to find the maximum number of 1s in the array 
nums= [1,1,0,1,1,1]

def binary_count(l1):
    maxsum=0
    count=0
    for i in range(len(l1)):
        if l1[i] == 1:
            count += 1
            maxsum= max(maxsum, count)
        else:
            count=0
    return maxsum

print(binary_count(nums))
