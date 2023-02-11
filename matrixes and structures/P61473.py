from yogi import read
from typing import TypeAlias

# Matrix type definition.
Row: TypeAlias = list[int]
Matrix: TypeAlias = list[Row]

def read_matrix(n: int) -> Matrix:
    """Reads the given square matrix of size (n x n), filled with integer numbers."""

    M: Matrix = [[0 for j in range(n)] for i in range(n)] 

    for i in range(n):
        for j in range(n):
            M[i][j] = read(int)

    return M

def is_symmetric(M: Matrix) -> bool:
    """Tells if a given square matrix is symmetric."""

    n = len(M)
    for i in range(n):
        for j in range(i + 1, n):
            if M[i][j] != M[j][i]:
                return False
    return True

def main() -> None:
    # Reads the size of the square matrix.
    n = read(int)
    M : Matrix = read_matrix(n)

    # Evaluating symmetry. 
    if is_symmetric(M):
        print('Yes', end = '\n')
    else:
        print('No', end = '\n')
    
if __name__ == '__main__':
    main()