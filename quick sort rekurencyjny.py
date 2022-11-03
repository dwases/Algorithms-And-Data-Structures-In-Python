# sortowanie szybkie
def partycja(tab, lewa, prawa):
    i = lewa-1
    pivot = tab[prawa]
    for j in range(lewa, prawa):
        if tab[j] >= pivot:  # by program dzialal rosnaco wystarczy zmienic kierunek nierownosci :P
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[prawa] = tab[prawa], tab[i+1]
    return i+1


def sortowanie(tab, lewa, prawa):
    if lewa < prawa:
        pivot = partycja(tab, lewa, prawa)
        sortowanie(tab, lewa, pivot-1)
        sortowanie(tab, pivot+1, prawa)


#tablica = input().split()
tablica = [928378, 10891, -11818, 8747, 1, 1, 2, 900, 488, -11111, 109, 788, 109]
print("wyjsciowa tablica:", tablica)
for i in range(len(tablica)):
    tablica[i] = int(tablica[i])
sortowanie(tablica, 0, len(tablica)-1)
print("posortowana tablica:", tablica)
c = input()
