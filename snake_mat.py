def snake_mat(array,m,n):
    for i in range(len(array)):
        if (i%2==0):
            for j in range(m):
                print(array[i][j])
        else:
            for k in reversed(range(m)):
                print(array[i][k])        




array = [[1, 2, 3, 4],
[12, 13, 14, 5],
[11, 16, 15, 6],
[10, 9, 8, 7]]

m = len(array)
n = len(array[0])
print(snake_mat(array,m,n))
