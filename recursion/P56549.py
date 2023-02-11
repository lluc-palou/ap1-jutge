from yogi import tokens

def escriu_en_binari(n: int) -> None:
    """Escriu el nombre que s'ha introduit en binari, 
    partint d'un nombre en base decimal."""

    if n >= 2:
        escriu_en_binari(n // 2)
    print(n % 2, end='')

def escriu_en_octal(n: int) -> None:
    """Escriu el nombre que s'ha introduit en octal, 
    partint d'un nombre en base decimal."""

    if n >= 8:
        escriu_en_octal(n // 8)
    print(n % 8, end='')

def escriu_en_hexadecimal(n: int) -> None:
    """Escriu el nombre que s'ha introduit en hexadecimal, 
    partint d'un nombre en base decimal."""
    
    if n < 16:
        if n < 10:
            print(n, end = '')

        elif n > 9 and n < 16:
            if n % 16 == 10:
                print('A', end='')
            elif n % 16 == 11:
                print('B', end='')
            elif n % 16 == 12:
                print('C', end='')
            elif n % 16 == 13:
                print('D', end='')
            elif n % 16 == 14:
                print('E', end='')
            else:
                print('F', end='')
        
    else:
        escriu_en_hexadecimal(n // 16)
        escriu_en_hexadecimal(n % 16)

def main() -> None:
    # Es llegeix una seqüència de nombres enters.
    for n in tokens(int):
        print(n, end=' = ')
        escriu_en_binari(n)
        print(',', end = ' ')
        escriu_en_octal(n)
        print(',', end = ' ')
        escriu_en_hexadecimal(n)
        print(end = '\n')
    
if __name__ == '__main__':
    main()