from dataclasses import dataclass

@dataclass
class Movie:
    title: str
    year: int
    stars: int
    earnings: float

def compare_movies(m1: Movie, m2: Movie) -> int:
    """Returns -1 whether m1 is better than m2, 1 if m2 is better and,
    0 if are the same, following the following criteria."""

    if m1.stars > m2.stars:
        return -1
    elif m1.stars < m2.stars:
        return 1
    else:
        if m1.earnings > m2.earnings:
            return -1
        elif m1.earnings < m2.earnings:
            return 1
        else:
            if m1.year > m2.year:
                return -1
            elif m1.year < m2.year:
                return 1
            else:
                return 0

def main() -> None:
    # Declaration and assignation of two example structures.
    m1 = Movie("Star Wars IV", 1977, 5, 100)
    m2 = Movie("The kid", 1921, 5, 100)
    print(compare_movies(m1, m2))

if __name__ == '__main__':
    main()