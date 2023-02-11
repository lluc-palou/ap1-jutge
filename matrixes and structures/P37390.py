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

def product(a: Matrix, b: Matrix) -> Matrix:
    """Returns the product of two square matrixes."""

    n = len(a)
    c: Matrix = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
            
    return c

def main() -> None:
    # Reads the size of the two square matrixes.
    n = read(int)
    a: Matrix = read_matrix(n)
    b: Matrix = read_matrix(n)
    print(product(a, b))
    
if __name__ == '__main__':
    main()