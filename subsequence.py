#O(n)
def subsequence(list1,seq):
    s=0
    for i in range(len(list1)):
        if i > len(list1):
            break
        if list1[i] == seq[s]:
            s +=1

    return s == len(seq)    


list1 = [5,1,22,25,6,-1,8,10]
seq = [1,6,-1,10]
print(subsequence(list1,seq))
