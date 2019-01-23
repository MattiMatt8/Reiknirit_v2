# Matthías Ólafur


# 3
def summa(m):
    if m != 1:
        return summa(m-1) + m**2
    else:
        return 1

#print("Svar summa:",summa(5))


# 4
def runa(m):
    if m != 1:
        m += runa(m-1)
    print(m)
    return m

#runa(6)

# 5
def þversumma(n):
    if n // 10 != 0:
        return þversumma(n//10) + n % 10
    else:
        return n % 10

#print("Svar þversumma:",þversumma(1209))

# 6