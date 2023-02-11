from yogi import read

def is_palindrome(s: str) -> bool:
    """Tells if the given word is a palindrome."""

    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False

    return True    

def main() -> None:
    # Reads a word.
    w = read(str)

    if is_palindrome(w):
        print('yes', sep = '', end = '\n')
    else:
        print('no', sep = '', end = '\n')

if __name__ == '__main__':
    main()