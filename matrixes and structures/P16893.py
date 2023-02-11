from yogi import read
from typing import TypeAlias

# Matrix type definition.
Row: TypeAlias = list[int]
Matrix: TypeAlias = list[Row]

def read_sudoku(n: int) -> Matrix:
    """Reads a possible answer of a Sudoku, in fact, a (9 x 9) matrix of 
    integer numbers from 1 to 9."""

    Sudoku : Matrix = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            Sudoku[i][j] = read(int)

    return Sudoku

def check_repeated_numbers_in_a_row(Sudoku: Matrix, n: int) -> bool:
    """Tells whether there are repeated numbers in the same row."""

    for i in range(n):
        seen_numbers = [0 for _ in range(n + 1)]

        for j in range(n):
            if seen_numbers[Sudoku[i][j]] == 1:
                return True
            else:
                seen_numbers[Sudoku[i][j]] = 1
    
    return False

def check_repeated_numbers_in_a_column(Sudoku: Matrix, n: int) -> bool:
    """Tells whether there are repeated numbers in the same column."""

    for j in range(n):
        seen_numbers = [0 for _ in range(n + 1)]

        for i in range(n):
            if seen_numbers[Sudoku[i][j]] == 1:
                return True
            else:
                seen_numbers[Sudoku[i][j]] = 1
    
    return False

def check_repeated_numbers_in_a_submatrix(Sudoku: Matrix, a: int, b: int, n: int) -> bool:
    """Tells whether there are repeated numbers in a submatrix."""

    m = 3
    seen_numbers = [0 for _ in range(n + 1)]
    c = b

    for i in range(m):
        if i > 0:
            a += 1
            c = b
        for j in range(m):
            if j > 0:
                c += 1
            if seen_numbers[Sudoku[a][c]] == 1:
                return True
            else:
                seen_numbers[Sudoku[a][c]] = 1

    return False

def check_submatrix(Sudoku: Matrix, n: int) -> bool:
    """Tells whether there are repeated numbers in some submatrix of the answer."""

    m = 3
    a = 0

    for i in range(m):
        a = 3 * i
        b = 0
        for j in range(m):
            if j > 0:
                b += 3
            if check_repeated_numbers_in_a_submatrix(Sudoku, a, b, n):
                return True

    return False
                    
def is_solution(Sudoku: Matrix) -> bool:
    """Tells if a given answer of a Sudoku follows its rules."""

    n = len(Sudoku)

    if check_repeated_numbers_in_a_row(Sudoku, n):
        return False
    if check_repeated_numbers_in_a_column(Sudoku, n):
        return False
    if check_submatrix(Sudoku, n):
        return False

    return True

def main() -> None:
    # Reads several cases that have to be checked, more specifically (n).
    c = read(int)

    for _ in range(c):
        Sudoku : Matrix = read_sudoku(9)

        if is_solution(Sudoku):
            print('yes', end = '\n')
        else:
            print('no', end = '\n')

if __name__ == '__main__':
    main()