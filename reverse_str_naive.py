
#Naive approach
def reverse_str(test):
    res = ""
    for i in test:
        res = i + res
    return res  

def test_palindrome(test):
    if reverse_str(test) == test:
        return True
    else:
        return False    

#two Pointer approach
def test_palindrome(test):
    i = 0
    j=len(test)-1

    while(i<j):
        if test[i] != test[j]:
            return False

        i+=1
        j-=1    

    return True        

test = 'abba'
print(test_palindrome(test))
