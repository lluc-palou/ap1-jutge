def is_leap_year(year: int) -> bool:
    """Indica si l'any proporcionat és any de traspàs."""
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and (year // 100) % 4 == 0:
        return True
    else:
        return False
