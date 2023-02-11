from yogi import read

# Lectura de les dades d'entrada.
h = read(int)
m = read(int)
s = read(int)

# Lòigca del programa.
s = s + 1

if s == 60:
    s = 0
    m = m + 1
    if m == 60:
        m = 0
        h = h + 1
        if h == 24:
            h = 0

# Format de sortida de l'hora.
print("%02d" % h, "%02d" % m, "%02d" % s, sep = ":")