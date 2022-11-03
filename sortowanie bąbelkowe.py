# sortowanie babelkowe
def sortowanie(tab):
    n = len(tab)
    while n > 1:
        for i in range(n-1):
            if tab[i] < tab[i+1]:  # jak sie zmieni znak rownosci na druga strone to bedzie sortowanie w druga strone :P
                tab[i], tab[i+1] = tab[i+1], tab[i]
        n -= 1
    return tab


#tablica = input().split()
tablica = [928378, 10891, -11818, 8747, 1, 1, 2, 900, 488, -11111, 109, 788, 109]
print("wyjsciowa tablica:", tablica)
for i in range(len(tablica)):
    tablica[i] = int(tablica[i])
tablica = sortowanie(tablica)
print("posortowana tablica:", tablica)
#c = input()
if None:
    print('hello')
else:
    print('no')
