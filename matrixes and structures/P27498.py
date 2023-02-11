from yogi import read
from typing import TypeAlias

# Matrix type definition.
Row: TypeAlias = list[int]
Matrix: TypeAlias = list[Row]

def read_matrix(n: int, m: int) -> Matrix:
    """Reads a matrix of natural numbers with the given size (n x m)."""

    M: Matrix = [[0 for j in range(m)] for i in range(n)] 

    for i in range(n):
        for j in range(m):
            M[i][j] = read(int)

    return M

def transpose(M: Matrix) -> Matrix:
    """Returns the given matrix transposed, assuming it is an square matrix."""

    n = len(M)
    for i in range(n):
        for j in range(i + 1, n):
             M[i][j], M[j][i] = M[j][i], M[i][j]
    
    return M

def main() -> None:
    # First, reads the number of rows and columns, then,
    # reads the given matrix.
    n = read(int)
    m = read(int)
    M : Matrix = read_matrix(n, m)
    M = transpose(M)
    print(M)

if __name__ == '__main__':
    main()