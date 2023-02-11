from yogi import read
from typing import TypeAlias

# Matrix type definition.
Matrix: TypeAlias = list[list[int]]

def read_matrix(r: int, c: int) -> Matrix:
    """Reads and returns the given matrix with dimensions (r x c)"""

    M: Matrix = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            M[i][j] = read(int)
    
    return M

def zig_zag_traversal(M: Matrix) -> bool:
    """Tells whether for the given matrix the zig-zag traversal is strictly increasing."""

    r, c = len(M), len(M[0])

    # Exceptional case.
    if r == 1 and c == 1:
        return True

    for j in range(c):
        if j == 0:
            last_element = M[0][0]

            for i in range(1, r):
                if M[i][j] <= last_element:
                    return False
                last_element = M[i][j]
            
        elif j % 2 == 0:
            for i in range(r):
                if M[i][j] <= last_element:
                    return False
                last_element = M[i][j]
            
        else:
            for i in range(r - 1, -1, -1):
                if M[i][j] <= last_element:
                    return False
                last_element = M[i][j]
    
    return True

def main() -> None:
    # Reads several cases.
    case = 0
    r = read(int)

    while r is not None:
        case += 1
        c = read(int)
        M: Matrix = read_matrix(r, c)

        if zig_zag_traversal(M):
            print('matriu ', case, ': ', 'si', sep = '', end = '\n')
        else:
            print('matriu ', case, ': ', 'no', sep = '', end = '\n')

        r = read(int)

if __name__ == '__main__':
    main()