from yogi import read

def is_increasing(n: int) -> bool:
    """Indica si el nombre introduit es creixent, és a dir, si 
    cada dígit és més petit o igual que el dígit de l'esquerre."""
    if n < 10:
        return True
    else:
        ultim_digit = n % 10
        n = n // 10
        penultim_d = n % 10
        if ultim_digit >= penultim_d:
            return is_increasing(n)
        else:
            return False
"""
def main() -> None:
    # Es llegeix un nombre natural.
    n = read(int)
    if is_increasing(n):
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    main()
"""