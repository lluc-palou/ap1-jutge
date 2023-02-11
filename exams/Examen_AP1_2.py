from typing import TypeAlias

# Definition of matrix type.
Row : TypeAlias = list[int]
Matrix : TypeAlias = list[Row]

def sum_upper_left_submatrix(Matrix: Matrix, i: int, j: int) -> int:
    """Returns the sum of the elements that are in the upper left submatrix."""

    sum = 0

    for x in range(i):
        for y in range(j):
            sum += Matrix[x][y]
    
    return sum

def sum_lower_right_submatrix(Matrix: Matrix, i: int, j: int) -> int:
    """Returns the sum of the elements that are in the lower right submatrix."""

    f = len(Matrix)
    c = len(Matrix)
    sum = 0

    for x in range(i, f):
        for y in range(j, c):
            sum += Matrix[x][y]

    return sum

def balanced_matrix(Matrix: Matrix, i: int, j: int) -> bool:
    """Tells whether the given matrix is balanced, according to 
    the balanced matrix definition explained in the statement."""

    if sum_upper_left_submatrix(Matrix, i, j) != sum_lower_right_submatrix(Matrix, i, j):
        return False

    return True 