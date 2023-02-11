from yogi import read
from typing import TypeAlias

# Matrix type definition.
Row : TypeAlias = list[int]
Matrix : TypeAlias = list[Row]

def read_square(n: int) -> Matrix:
    """Reads the given Magic square of order n."""

    Square : Matrix = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            Square[i][j] = read(int)
    
    return Square

def chech_columns(Square: Matrix, same_number: int) -> bool:
    """Tells whether the columns of the square add up to the same number than 
    the rows and diagonals."""

    n = len(Square)

    for j in range(n):
        sum = 0
        for i in range(n):
            sum += Square[i][j]

        if sum != same_number:
            return False

    return True

def chech_diagonal(Square: Matrix, same_number: int) -> bool:
    """Tells whether the main diagonal add up to the same number than the rows, 
    the columns and the anti-diagonal."""

    n = len(Square)
    sum = 0

    for i in range(n):
        sum += Square[i][i]

    if sum != same_number:
        return False

    return True

def chech_anti_diagonal(Square: Matrix, same_number: int) -> bool:
    """Tells whether the anti-diagonal add up to the same number than the rows, 
    columns and diagonal."""

    n = len(Square)
    sum = 0
    
    for i in range(n - 1, -1, -1):
            sum += Square[i][n - i - 1]

    if sum != same_number:
        return False

    return True

def check_magic_square(Square: Matrix) -> bool:
    """Tells whether the given square is a Magic square."""

    n = len(Square)

    # Checks that all numbers from 1 to n^2 appear in the square while checking 
    # that all rows add up to the same number.
    seen_numbers = [0 for _ in range(n*n + 1)]
    first_row = True
    same_number = 0

    for i in range(n):
        sum = 0
        for j in range(n):
            sum += Square[i][j]

            if seen_numbers[Square[i][j]] == 1:
                return False
            else:
                seen_numbers[Square[i][j]] = 1

        if first_row:
            same_number = sum
            first_row = False
        
        elif sum != same_number:
            return False

    if not chech_columns(Square, same_number):
        return False

    if not chech_diagonal(Square, same_number):
        return False

    if not chech_anti_diagonal(Square, same_number):
        return False
   
    return True
    
def main() -> None:
    # Reads several cases.
    square_order = read(int)

    while square_order is not None:
        Square : Matrix = read_square(square_order)

        if check_magic_square(Square):
            print('yes', end = '\n')
        else:
            print('no', end = '\n')

        square_order = read(int)

if __name__ == '__main__':
    main()