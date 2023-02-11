from yogi import *

def max4(a: int, b: int, c: int, d:int) -> int:
    """Retorna el màxim de 4 nombres enters donats"""
    return max2(max2(a, b), max2(c, d))
    
def max2(a: int, b: int) -> int:
    """Retorna el màxim de dos nombres enters donats."""
    if a > b:
        return a
    else:
        return b

def main():
    # Es llegeixen 4 nombres enters.
    a = read(int)
    b = read(int)
    c = read(int)
    d = read(int)
    print(max4(a, b, c, d))

if __name__ == '__main__':
    main()