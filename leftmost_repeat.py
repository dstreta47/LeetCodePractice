
def leftmost(test):
    char = [-1]*256
    res = 99999

    for i in range(len(test)):
        if char[ord(test[i])] == -1:
            char[ord(test[i])] =i
        else:
            res = min(res,char[ord(test[i])])   
    return res         

test = 'abcdefgbac'
print(leftmost(test))
