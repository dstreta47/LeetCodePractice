from collections import Counter

def anagram(s1,s2):

    if set(s1) == set(s2):
        print("its anagram")
    else:
        print("its not anagram")    

def anagram2(s1,s2):

    if Counter(s1) == Counter(s2):
        print("its anagram")
    else:
        print("its not anagram")           


#anagram2('aabca','acaba')


print(Counter('aabca'))
