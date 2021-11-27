def matrix_spiral(array):
    SR = 0
    SC = 0
    ER = len(array)-1
    EC = len(array[0])-1
    res = []
    while SR<=ER and SC<=EC:
        for col in range(SC,EC+1):
            res.append(array[SR][col])
        for row in range(SR+1,ER+1):
            res.append(array[row][EC])
        for col in reversed(range(EC,SC)):
            res.append(array[ER][col])
        for row in reversed(range(SR+1,ER)):
            res.append(array[row][SC])   
        SR +=1
        SC +=1
        ER -=1
        EC -=1   
    return res    
array = [[1, 2, 3, 4],
[12, 13, 14, 5],
[11, 16, 15, 6],
[10, 9, 8, 7]]
print(matrix_spiral(array))
