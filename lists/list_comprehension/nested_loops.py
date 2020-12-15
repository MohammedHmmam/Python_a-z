#Suppose, we need to compute the transpose of a matrix that require nested for loop
# let's see how it is done using normal for loop first


#==> Transpose of Matrix using Nested Loops
transposed = []
matrix = [ [1,2,3,4], [5,6,7,8] ]
for i in range( len( matrix[0] ) ):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

#==> Transpose of a matrix using list comprehension
matrix2 = [[1,2] , [3,4] , [5,6] , [7,8]]
transpose = [[row[i] for row in matrix2] for i in range(2)]
print(transpose)