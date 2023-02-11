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

def answer_question(q: str, M: Matrix) -> None:
    """Answers questions about the matrix, concerning its rows. columns and elements."""

    if q == 'row':
        r = read(int)
        print('row ', r, ': ', sep = '', end = '')
        for i in range(len(M[0]) - 1):
            print(M[r - 1][i], end = ' ')
        print(M[r - 1][len(M[0]) - 1], sep = '', end = '\n')
    
    if q == 'column':
        c = read(int)
        print('column ', c, ': ', sep = '', end = '')
        for j in range(len(M) - 1):
            print(M[j][c - 1], end = ' ')
        print(M[len(M) - 1][c - 1], sep = '', end = '\n')

    if q == 'element':
        r = read(int)
        c = read(int)
        print('element ', r,' ', c, ': ', M[r - 1][c - 1], sep = '', end = '\n')

def main() -> None:
    # First, reads the number of rows and columns, then,
    # reads the given matrix.
    n = read(int)
    m = read(int)
    M : Matrix = read_matrix(n, m)

    # Reads questions about the matrix.
    q = read(str)
    while q is not None:
        answer_question(q, M)
        q = read(str)

if __name__ == '__main__':
    main()
