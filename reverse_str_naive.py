
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



test = 'abba'
print(test_palindrome(test))
