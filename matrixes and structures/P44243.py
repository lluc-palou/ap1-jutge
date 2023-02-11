from yogi import read
from typing import TypeAlias

# Matrix type definition.
Row: TypeAlias = list[str]
Matrix: TypeAlias = list[Row]

def spiral(n: int) -> Matrix:
    """Returns a (n x n) spiral in a matrix of the same size."""

    Spiral : Matrix = [["." for j in range(n)] for i in range(n)] # Initializes an empty matrix, without spiral.
    counter = n # Counts the number of x's to set for each iteration of the loop.
    x, y = n - 1, 0 # Corresponds to the first x position for each iteration.
    row_right = True
    column_up = True

    while counter >= 1:
        # Moving right.
        if row_right and column_up:
            for _ in range(counter):
                Spiral[x][y] = 'X'
                y += 1
            y -= 1    
            x -= 1
            row_right = False
        
        # Moving left.
        elif not row_right and not column_up:
            for _ in range(counter):
                Spiral[x][y] = 'X'
                y -= 1
            y += 1    
            x += 1
            row_right = True
        
        # Moving up.
        elif not row_right and column_up:
            for _ in range(counter):
                Spiral[x][y] = 'X'
                x -= 1
            x += 1    
            y -= 1
            column_up = False
        
        # Moving down.
        elif row_right and not column_up:
            for _ in range(counter):
                Spiral[x][y] = 'X'
                x += 1
            x -= 1    
            y += 1
            column_up = True

        counter -= 1

    return Spiral
   
def print_spiral(Spiral: Matrix) -> None:
    """Prints the given spiral."""

    n = len(Spiral)

    for i in range(n):
        for j in range(n - 1):
            print(Spiral[i][j], sep = '', end = '')
        print(Spiral[i][n - 1], sep = '', end = '\n')
    print(end = '\n')

def main() -> None:
    # Reads a sequence of natural numbers ended with 0.
    n = read(int)
    while n > 0:
        Spiral : Matrix = spiral(n)
        print_spiral(Spiral)
        n = read(int)

if __name__ == '__main__':
    main()