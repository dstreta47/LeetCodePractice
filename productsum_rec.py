def productsum(array,m=1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum+=productsum(element,m+1)
        else:
            sum+=element

    return sum * m        


productsum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])    
