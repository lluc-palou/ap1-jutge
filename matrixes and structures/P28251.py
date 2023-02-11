from dataclasses import dataclass
from typing import TypeAlias

@dataclass
class Provincia:
    nom: str
    capital: str
    habitants: int
    area: int
    pib: float

@dataclass
class Pais:
    nom: str
    capital: str
    provincies: list[Provincia]

Paisos: TypeAlias = list[Pais]

def habitants(paisos: Paisos, x: float) -> int:
    """Retorna la suma dels habitants d'aquells paisos en (paisos)
    que tinguin almenys 2 províncies amb producte interior brut 
    inferior o igual que (x)."""

    suma_habitants = 0

    for pais in paisos:
        comptador_provincies = 0

        for provincia in pais.provincies:
            if provincia.pib <= x:
                comptador_provincies += 1

        if comptador_provincies >= 2:
            for provincia in pais.provincies:
                suma_habitants += provincia.habitants

    return suma_habitants

def main() -> None:
    # Declaration and assignation of two example structures.
    pr1 = Provincia("Girona", "Girona", 2, 45, 75000)
    pr2 = Provincia("Barcelona", "Barcelona", 4, 25, 120000)
    pr3 = Provincia("Tarragona", "Tarragona", 1, 21, 34000)
    pr4 = Provincia("Lleida", "Lledia", 1, 67, 50000)
    pr5 = Provincia("Terol", "Terol", 1, 125, 10000)
    pr6 = Provincia("Alacant", "Alacant", 2, 30, 40000)
    pr7 = Provincia("Lugo", "Lugo", 1, 24, 58000)
    pr8 = Provincia("Palencia", "Palencia", 1, 52, 45000)

    p1 = Pais("catalunya", "Barcelona", [pr1, pr2, pr3, pr4])
    p2 = Pais("espanya", "Madrid", [pr5, pr6, pr7, pr8])

    P: Paisos = [p1, p2]

    print(habitants(P, 60000))

if __name__ == "__main__":
    main()