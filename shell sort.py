# sortowanie babelkowe
def sortowanie(d):
    # K01
    # print(d)
    h = 1
    # K01

    # K02
    while h < n:
        h = 3*h+1
    # K02

    # K03
    h = h//9
    # K03

    # K04
    if h == 0:
        h = 1
    # K04
    # dotad powinno stykac :/
    # K05
    while h > 0:
        # K06
        for j in range(n-h-1, -1, -1):  # n-h lub n-h-1 - jedno z dwoch... raczej n-h?
            # K07
            x = d[j]
            i = j + h
            # K07
            # K08
            while i < n and x > d[i]:
                d[i-h] = d[i]
                # print(d[i-h])
                i = i + h
            # K08
            # K09
            d[i-h] = x
            # print(d[i-h])
            # K09
        # K10
        h = h//3
        # K10
        print('posortowana tablica', [d[p] for p in range(len(d)-1, -1, -1)])


#tablica = input().split()
tablica = [928378, 10891, -11818, 8747, 1, 1, 2, 900, 488, -11111, 109, 788, 109]
n = len(tablica)
print("wyjsciowa tablica:", tablica)
for i in range(len(tablica)):
    tablica[i] = int(tablica[i])
tablica = sortowanie(tablica)
#print("posortowana tablica:", tablica)
# for eken in tablica:
#    print(eken)
c = input()
