from yogi import read

# Es llegeixen els nombres enters x i y:
x = read(int)
y = read(int)

# Programa principal.
if x > y:
    i = x

    while i >= y:
        print(i)
        i = i - 1

else:
    i = y
    
    while i >= x:
        print(i)
        i = i - 1
