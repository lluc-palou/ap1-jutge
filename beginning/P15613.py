from yogi import read

# Es llegeix un nombre enter.
t = read(int)

# Lògica del programa.
if t < 10:
    print("it's cold")
elif t > 30:
    print("it's hot")
else:
    print("it's ok")

if t <= 0:
    print("water would freeze")
if t >= 100:
    print("water would boil")