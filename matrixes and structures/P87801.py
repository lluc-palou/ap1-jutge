from yogi import read
from typing import TypeAlias

# Matrix type definition.
Matrix_1: TypeAlias = list[list[str]]
Matrix_2: TypeAlias = list[list[int]]

def read_letters(r: int, c: int) -> Matrix_1:
    """Reads the given matrix of letters with dimensions (r x c)."""

    M: Matrix_1 = [['.' for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            M[i][j] = read(str)

    return M

def read_points(r: int, c: int) -> Matrix_2:
    """Reads the given matrix of points with dimensions (r x c)."""

    M: Matrix_2 = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            M[i][j] = read(int)

    return M

def max_score(Letters: Matrix_1, Points: Matrix_2, word: str) -> int:
    """Returns the maximal number of points that can be achieved placing the word horizontally or vertically."""

    r = len(Letters)
    c = len(Letters[0])
    current_score = 0
    max_score = 0
    word_lenght = len(word)
    
    # Sequential scan of the letters.
    # Assuming word is placed horizontally.
    for i in range(r):
        for j in range(c - word_lenght + 1):
            word_found = True
            k = 0
            while k >= 0 and k < word_lenght and word_found:
                current_score += Points[i][j + k]

                if Letters[i][j + k] != word[k]:
                    word_found = False

                k += 1

            if word_found and max_score < current_score:
                max_score = current_score
            
            current_score = 0
    
    # Assuming word is placed vertically.
    for j in range(c):
        for i in range(r - word_lenght + 1):
            word_found = True
            k = 0
            while k >= 0 and k < word_lenght and word_found:
                current_score += Points[i + k][j]

                if Letters[i + k][j] != word[k]:
                    word_found = False

                k += 1

            if word_found and max_score < current_score:
                max_score = current_score
            
            current_score = 0

    return max_score

def main() -> None:
    # Reads serveral cases.
    r = read(int)

    while r is not None:
        c = read(int)
        Letters: Matrix_1 = read_letters(r, c)
        Points: Matrix_2 = read_points(r, c)
        n_words = read(int)

        for _ in range(n_words):
            word = read(str)

            if max_score(Letters, Points, word) != 0:
                print(max_score(Letters, Points, word), sep = '', end = '\n')
            else:
                print('no', sep = '', end = '\n')

        r = read(int)

if __name__ == '__main__':
    main()