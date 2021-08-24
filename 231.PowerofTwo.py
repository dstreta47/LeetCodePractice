class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return 1
      
    # if power is 1 then number is
    # returned
        elif n == 1:
            return n
      
        else:
            return (n*power(n, n-1))
        
