from yogi import *

def missatge(qui: str, verb: str, cops: int, fem: bool) -> None:
    """Escriu el missatge que s'adequa als paràmetres d'entrada."""
    if fem:
        print('Na', qui, end = ' ')

        if cops == 0:
            verb = verb + "."
            print('no ha', verb, end = '\n')
        else:
            if cops == 1:
                print('ha', verb, cops, 'cop.', end = '\n')
            else:
                print('ha', verb, cops, 'cops.', end = '\n')
    else:
        print('En', qui, end = ' ')

        if cops == 0:
            verb = verb + "."
            print('no ha', verb, end = '\n')
        else:
            if cops == 1:
                print('ha', verb, cops, 'cop.', end = '\n')
            else:
                print('ha', verb, cops, 'cops.', end = '\n')

def main() -> None:
    # Es llegeix un nom, un verb, un nombre enter i un booleà.
    qui = read(str)
    verb = read(str)
    cops = read(int)
    fem = read(int)
    missatge(qui, verb, cops, fem)

if __name__ == '__main__':
    main()