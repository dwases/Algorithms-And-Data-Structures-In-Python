#sortowanie przez scalanie


def sortowanie(tab):
    if len(tab) > 1:
    #1
        punkt_podzialu = len(tab)//2
        prawa_tablica = tab[punkt_podzialu:]
        lewa_tablica = tab[:punkt_podzialu]
    #2
        sortowanie(lewa_tablica)
    #3
        sortowanie(prawa_tablica)

    #obszar testowy
        a = 0
        b = 0
        c = 0
        while a < len(lewa_tablica) and b < len(prawa_tablica):
            if lewa_tablica[a] > prawa_tablica[b]:              #zeby program sortowal w druga strone wystarczy zmienic kierunek nierownosci :P
                tab[c] = lewa_tablica[a]
                a += 1
            else:
                tab[c] = prawa_tablica[b]
                b += 1
            c += 1
        while a < len(lewa_tablica):
            tab[c] = lewa_tablica[a]
            a += 1
            c += 1
        while b < len(prawa_tablica):
            tab[c] = prawa_tablica[b]
            b += 1
            c += 1


    #4
    #4.1
    #i = 0       #dla lewej
    #j = 0       #dla prawej
    #k = 0
    #n = len(lewa_tablica)
    #m = len(prawa_tablica)
    #odtad ma powtarzac prace dopoki wszystkie wyrazy nie sa w c
    #scalona_tablica = []
    #while len(scalona_tablica)!=(n+m):
        #4.2
    #    if i>n:
    #        for iter in range(j,-1,-1):
    #            scalona_tablica.append(prawa_tablica[j])
    #        break
        #4.3
    #    if j>m:
    #        for iter in range(j,-1,-1):
    #            scalona_tablica.append(lewa_tablica[i])
    #        break
        #4.4
    #    if lewa_tablica[i]<=prawa_tablica[j]:
    #        scalona_tablica.append(lewa_tablica[i])
    #    else:
    #        scalona_tablica.append(prawa_tablica[j])
    #return scalona_tablica
#tablica = input().split()
tablica = [928378, 10891, -11818, 8747, 1, 1,2,900,488,-11111,109,788,109]
print("wyjsciowa tablica:", tablica)
for i in range(len(tablica)):
    tablica[i] = int(tablica[i])
#tablica = sortowanie(tablica)
sortowanie(tablica)
print("posortowana tablica:", tablica)
c = input()
