def nonrep_leftmost(test):
    char = [-1]*256

    for i in range(len(test)):
        if char[ord(test[i])] == -1:
            char[ord(test[i])] = i
        else:
          char[ord(test[i])] = -2      

    return char





test = 'abcdefgbac'
char = nonrep_leftmost(test)
res = 9999
for i,j in enumerate(char):
    if j>0:
        res = min(res,j)

print(test[res])        
