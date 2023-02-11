from yogi import read

# Es llegeixen dos nombres enters a i b.
a = read(int)
b = read(int)

# Programa principal.
if a < b:
    while a < b:
        print(a, end = ",")
        a = a + 1
    print(b)
elif a == b:
    print(a)
else:
    print(end = "\n")
