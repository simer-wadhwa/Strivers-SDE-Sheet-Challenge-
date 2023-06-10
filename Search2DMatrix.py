def searchMatrix(mat: [[int]], target: int) -> bool:
    # Write your code here.
    r = len(mat) - 1
    col = len(mat[0]) - 1
    j = 0

    while j <= r and col >= 0:
        if mat[j][col] == target:
            return True

        elif mat[j][col] < target:
            j += 1

        else:
            col -= 1

    return False

