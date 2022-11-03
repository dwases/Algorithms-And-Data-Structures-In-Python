import heapq
def sortowanie(tab):
    sterta = []
    for element in tab:
        heapq.heappush(sterta, element)
    return [heapq.heappop(sterta) for i in range(len(sterta))]

tablica = [928378, 10891, -11818, 8747, 1, 1,2,900,488,-11111,109,788,109]
print("wyjsciowa tablica:", tablica)
for i in range(len(tablica)):
    tablica[i] = -1*int(tablica[i])
tablica = sortowanie(tablica)
for i in range(len(tablica)):
    tablica[i] = -1*int(tablica[i])
print("posortowana tablica:", tablica)
c = input()
