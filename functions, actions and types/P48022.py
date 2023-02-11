from yogi import *
from math import *
from turtle import *

def dibuixar_rellotge(h: int, m: int) -> None:
    """Dibuixa un rellotge il·lustrant el temps d'entrada."""
    # Es dibuixa el cercle.
    penup()
    goto(0, -200)
    pendown()
    circle(200)
    penup()
    goto(0, 0)

    # Es dibuixen les ratlletes de les vores.
    for i in range(12):
        left(pi() / 6)
        forward(150)
        pendown()
        forward(50)
        penup()
        left(180)
        forward(200)
        left(180)
    left(pi() / 2)
    
    # Es dibuixen les busques.
    temps = h * 60 + m
    hores = True
    dibuixa_busca(temps, hores)
    hores = False
    dibuixa_busca(temps, hores)
    done()

def dibuixa_busca(temps: int, hores: bool) -> None:
    """Dibuixa les busques de les hores i els minuts."""
    if hores:
        h = temps / 2
        for i in range(h):
            right(pi() / 180)
        pendown()
        forward(pi() / 2)
        left(150)
        forward(25)
        left(120)
        forward(25)
        left(120)
        forward(25)
        right(pi() / 6)
        penup()
        goto(0, 0)

        for i in range(h):
            left(1)
    
    else:
        minuts = temps % 60
        for i in range(minuts):
            right(6)
        pendown()
        forward(140)
        left(150)
        forward(25)
        left(120)
        forward(25)
        left(120)
        forward(25)
        right(30)
        penup()
        goto(0, 0)


def main() -> None:
    # Es llegeixen l'hora i els minuts (ambdós nombres naturals).
    h = read(int)
    m = read(int)
    speed(0)
    radians()
    dibuixar_rellotge(h, m)

if __name__ == '__main__':
    main()