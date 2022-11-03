#sortowanie przez wybieranie

def sortowanie(tab):        #tab - tablica wyjsciowa
    sor_tab = []    #tablica z posortowanymi elementami, bedzie uzupelniana z tej wyjsciowej
    num0 = len(tab)
    while len(sor_tab)!=num0:
        for el in tab:
            if el == max(tab):          #jak sie zmieni max na min to bedzie sortowanie w druga strone :P
                sor_tab.append(el)
                tab.remove(el)
                break
    return sor_tab



#tablica = input().split()
tablica = [928378, 10891, -11818, 8747, 1, 1,2,900,488,-11111,109,788,109]
for i in range(len(tablica)):
    tablica[i] = int(tablica[i])
#for i in tablica:
#    print(i)
#dziala, sa inty
print("wyjsciowa tablica:", tablica)
tablica = sortowanie(tablica)
print("posortowana tablica:", tablica)
c = input()
