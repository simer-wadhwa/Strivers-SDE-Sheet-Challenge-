def printPascal(n: int):
    # Write your code here.
    # Return a list of lists.
    # matrix=[]

    matrix = [[0] * (i + 1) for i in range(n)]
    for i in range(n):
        matrix[i][0] = 1
        matrix[i][i] = 1
        for j in range(1, i):
            matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]

    return matrix