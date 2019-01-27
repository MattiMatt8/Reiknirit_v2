# Matthías Ólafur


#2 - Sauðakóðinn er í readme skjalinu
# def tugaTvi(n):
#    if n > 0:
#        return tugaTvi(n//2) + str(n%2)
#    return str(n%2)
#
# print("tuga í tví:",tugaTvi(25))


# 3
def summa(m):
    if m == 0:
        return 0
    if m != 1:
        return summa(m-1) + m**2
    else:
        return 1

#print("Svar summa:",summa(5))


# 4
def runa(m):
    if m == 0:
        return 0
    elif m != 1:
        m += runa(m-1)
    print(m, end=" ")
    return m

#runa(5)


# 5
def þversumma(n):
    if n // 10 != 0:
        return þversumma(n//10) + n % 10
    else:
        return n % 10

#print("Svar þversumma:",þversumma(1206))


# 6
def samnefnari(n,m):
    if m == 0:
        return n
    if n % m == 0:
        return m
    return samnefnari(m,n%m)

#print("Svar samnefnari:",samnefnari(12,60))