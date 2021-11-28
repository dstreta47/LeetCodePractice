def maxp(n,a,b,c):
    if n==0:
        return 0
    if n<0:
        return -1
    res = max(maxp(n-a,a,b,c),maxp(n-b,a,b,c),maxp(n-c,a,b,c))
    if res == -1:
        return -1
    res +=1
    return res
print(maxp(23,11,9,12))

