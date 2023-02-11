from yogi import read
from typing import TypeAlias

# Matrix type definition.
Row: TypeAlias = list[int]
Matrix: TypeAlias = list[Row]

def read_matrix(n: int, m: int) -> Matrix:
    """Reads the given matrix of size (n x m), filled with integer numbers."""

    M: Matrix = [[0 for j in range(m)] for i in range(n)] 

    for i in range(n):
        for j in range(m):
            M[i][j] = read(int)

    return M

def product(a: Matrix, b: Matrix) -> Matrix:
    """Returns the product of two matrixes of sizes (p x q) and (q x r)."""

    p = len(a)
    q = len(a[0])
    r = len(b[0])
    c: Matrix = [[0 for j in range(r)] for i in range(p)]

    for i in range(p):
        for j in range(r):
            for k in range(q):
                c[i][j] += a[i][k] * b[k][j]
            
    return c

def main() -> None:
    # Reads the size of the first matrix.
    p = read(int)
    q = read(int)
    a: Matrix = read_matrix(p, q)
    print(a)

    # Reads the size of the second matrix.
    r = read(int)
    b: Matrix = read_matrix(q, r)
    print(b)

    print(product(a, b))
    
if __name__ == '__main__':
    main()