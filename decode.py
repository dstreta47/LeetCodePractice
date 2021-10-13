'''
You are given an encoded string  and number of rows, Convert it to original string
  
 Input: mnesi___ya__k____mime  N = 3
  
 Output : my name is mike

 Explanation : Read the matrix in a diagonal way starting from [0][0] index until the end of row and start from the top
 again to decode it. _ are treated as space.
 
 m n e s i _  _
      
  _ y a _ _ k _
 	   
  _ _ _ m i m e

'''

inp = 'mnesi___ya__k____mime'
n = 3

# generate the matrix
mat = []
start = 0
for i in range(n):
    end = start + (len(inp)//n)
    mat.append(inp[start:end])
    start = end

# Decode the original string using generated matrix
x = n
y = len(inp)//n
i = 0

ans = ''
for j in range(y):
    while(i<x and j<y):
        if(mat[i][j]=='_'):
            ans+=' '
        else:
            ans+=mat[i][j]
        i+=1
        j+=1

    i=0

print(ans)
