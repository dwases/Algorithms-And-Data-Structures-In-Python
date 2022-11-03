# sortowanie przez wstawianie
def sortowanie(tab):
    sor_tab = []
    sor_tab.append(tab.pop())
    # print(sor_tab)     #krok 1 dziala
    # print(tab)         #krok 1 dziala
    for el in tab:
        # print(sor_tab)
        for i in range(len(sor_tab)):
            if el >= sor_tab[i]:  # jak sie odwroci nierownosc to sortowanie jest w druga strone
                sor_tab.insert(i, el)
                break
            if i == (len(sor_tab)-1):
                sor_tab.append(el)
        # print('el=',el)
#        tab.remove(el)
    return sor_tab


#tablica = [928378, 10891, -11818, 8747, 1, 1, 2, 900, 488, -11111, 109, 788, 109, 1]
tablica = input().split()
for i in range(len(tablica)):
    tablica[i] = int(tablica[i])
# for i in tablica:
#    print(i)
# dziala, sa inty
print("wyjsciowa tablica:", tablica)
tablica = sortowanie(tablica)
print("posortowana tablica:", tablica)
c = input()
