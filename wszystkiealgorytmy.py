import time
import random
import math
import sys
import copy
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
# globale do porownan
ilosc_porownan_heap = 0
ilosc_porownan_quick = 0
ilosc_porownan_shell = 0
ilosc_porownan_bubble = 0
# ilosc_porownan_merge = 0   tego ma nie byc, ale jest tu zebym przypadkiem nie dodal jak zapomne
ilosc_porownan_insertion = 0
ilosc_porownan_selection = 0


# globalne do swapow
ilosc_swapow_heap = 0
ilosc_swapow_quick = 0
ilosc_swapow_shell = 0
ilosc_swapow_bubble = 0
# ilosc_swapow_merge = 0   tego ma nie byc, ale jest tu zebym przypadkiem nie dodal jak zapomne
ilosc_swapow_insertion = 0
ilosc_swapow_selection = 0

# globalne do czasu obliczen
czas_heap = 0
czas_quick = 0
czas_shell = 0
czas_bubble = 0
czas_merge = 0
czas_insertion = 0
czas_selection = 0
####################################################################################################
sys.setrecursionlimit(10**9)

#                 888                     d8   ,e,                                                  d8
# d88~\  e88~~8e  888  e88~~8e   e88~~\ _d88__  "   e88~-_  888-~88e        d88~\  e88~-_  888-~\ _d88__
# C888   d888  88b 888 d888  88b d888     888   888 d888   i 888  888       C888   d888   i 888     888
# Y88b  8888__888 888 8888__888 8888     888   888 8888   | 888  888        Y88b  8888   | 888     888
#  888D Y888    , 888 Y888    , Y888     888   888 Y888   ' 888  888         888D Y888   ' 888     888
# \_88P   "88___/  888  "88___/   "88__/  "88_/ 888  "88_-~  888  888       \_88P   "88_-~  888     "88_/
#
# sortowanie przez wybieranie


def sortowanie_przez_wybieranie(tab):  # tab - tablica wyjsciowa
    global ilosc_swapow_selection
    global ilosc_porownan_selection
    global czas_selection
    tab1 = []
    for i in range(len(tab)):
        tab1.append(tab[i])
    t0 = time.time()
    sor_tab = []  # tablica z posortowanymi elementami, bedzie uzupelniana z tej wyjsciowej
    num0 = len(tab1)
    while len(sor_tab) != num0:
        for el in tab1:
            ilosc_porownan_selection += 1
            if el == max(tab):  # jak sie zmieni max na min to bedzie sortowanie w druga strone :P
                ilosc_swapow_selection += 1
                sor_tab.append(el)
                tab1.remove(el)
                break
    czas_selection = time.time() - t0
    # return sor_tab

# sortowanie przez wstawianie
# ,e,                                    d8   ,e,                                                  d8
# "  888-~88e  d88~\  e88~~8e  888-~\ _d88__  "   e88~-_  888-~88e        d88~\  e88~-_  888-~\ _d88__
# 888 888  888 C888   d888  88b 888     888   888 d888   i 888  888       C888   d888   i 888     888
# 888 888  888  Y88b  8888__888 888     888   888 8888   | 888  888        Y88b  8888   | 888     888
# 888 888  888   888D Y888    , 888     888   888 Y888   ' 888  888         888D Y888   ' 888     888
# 888 888  888 \_88P   "88___/  888     "88_/ 888  "88_-~  888  888       \_88P   "88_-~  888     "88_/


def sortowanie_przez_wstawianie(tab):
    global ilosc_swapow_insertion
    global ilosc_porownan_insertion
    global czas_insertion
    t0 = time.time()
    sor_tab = []
    # print(tab)
    sor_tab.append(tab.pop())
    # print(sor_tab)     #krok 1 dziala
    # print(tab)         #krok 1 dziala
    for el in tab:
        # print(sor_tab)
        for i in range(len(sor_tab)):
            ilosc_porownan_insertion += 1
            if el >= sor_tab[i]:  # jak sie odwroci nierownosc to sortowanie jest w druga strone
                ilosc_swapow_insertion += 1
                sor_tab.insert(i, el)
                break
            if i == (len(sor_tab)-1):
                sor_tab.append(el)
        # print('el=',el)
#        tab.remove(el)
    czas_insertion = time.time() - t0
    return sor_tab

# sortowanie przez scalanie
#                                     /                                          d8
# 888-~88e-~88e  e88~~8e  888-~\ e88~88e  e88~~8e         d88~\  e88~-_  888-~\ _d88__
# 888  888  888 d888  88b 888    888 888 d888  88b       C888   d888   i 888     888
# 888  888  888 8888__888 888    "88_88" 8888__888        Y88b  8888   | 888     888
# 888  888  888 Y888    , 888     /      Y888    ,         888D Y888   ' 888     888
# 888  888  888  "88___/  888    Cb       "88___/        \_88P   "88_-~  888     "88_/
#                                Y8""8D


def sortowanie_przez_scalanie(tab):
    global czas_merge
    t0 = time.time()
    if len(tab) > 1:
        # 1
        punkt_podzialu = len(tab)//2
        prawa_tablica = tab[punkt_podzialu:]
        lewa_tablica = tab[:punkt_podzialu]
    # 2
        sortowanie_przez_scalanie(lewa_tablica)
    # 3
        sortowanie_przez_scalanie(prawa_tablica)

    # obszar testowy
        a = 0
        b = 0
        c = 0
        while a < len(lewa_tablica) and b < len(prawa_tablica):
            # zeby program sortowal w druga strone wystarczy zmienic kierunek nierownosci :P
            if lewa_tablica[a] > prawa_tablica[b]:
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
    czas_merge = time.time() - t0

# sortowanie babelkowe


def sortowanie_babelkowe(tab):
    global ilosc_swapow_bubble
    global ilosc_porownan_bubble
    global czas_bubble
    t0 = time.time()
    n = len(tab)
    while n > 1:
        for i in range(n-1):
            ilosc_porownan_bubble += 1
            if tab[i] < tab[i+1]:  # jak sie zmieni znak rownosci na druga strone to bedzie sortowanie w druga strone :P
                ilosc_swapow_bubble += 1
                tab[i], tab[i+1] = tab[i+1], tab[i]
        n -= 1
    czas_bubble = time.time()-t0
    return tab

# sortowanie shella


def sortowanie_shella(d):
    global ilosc_swapow_shell
    global ilosc_porownan_shell
    global czas_shell
    n = len(d)
    t0 = time.time()
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
            ilosc_porownan_shell += 1
            while i < n and x > d[i]:
                ilosc_swapow_shell += 1
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
        czas_shell = time.time()-t0
        # K10
        #print('posortowana tablica', [d[p] for p in range(len(d)-1, -1, -1)])

# sortowanie szybkie


def partycja(tab, lewa, prawa):
    global ilosc_swapow_quick
    global ilosc_porownan_quick
    i = lewa-1
    pivot = tab[prawa]
    for j in range(lewa, prawa):
        ilosc_porownan_quick += 1
        if tab[j] >= pivot:  # by program dzialal rosnaco wystarczy zmienic kierunek nierownosci :P
            i += 1
            ilosc_swapow_quick += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[prawa] = tab[prawa], tab[i+1]
    return i+1


def sortowanie_szybkie(tab, lewa, prawa):
    global czas_quick
    t0 = time.time()
    if lewa < prawa:
        pivot = partycja(tab, lewa, prawa)
        sortowanie_szybkie(tab, lewa, pivot-1)
        sortowanie_szybkie(tab, pivot+1, prawa)
    czas_quick = time.time()-t0
# globale do quick sorta
#0, len(tablica)-1

# heap sort              -----------------------------------------------------------------------------do uzupelnienia---------EDIT: juz nie tak w ogole------------------------------
# 888                                                                   d8
# 888-~88e  e88~~8e    /~~~8e  888-~88e         d88~\  e88~-_  888-~\ _d88__
# 888  888 d888  88b       88b 888  888b       C888   d888   i 888     888
# 888  888 8888__888  e88~-888 888  8888        Y88b  8888   | 888     888
# 888  888 Y888    , C888  888 888  888P         888D Y888   ' 888     888
# 888  888  "88___/   "88_-888 888-_88"        \_88P   "88_-~  888     "88_/
#                             888


# TUTAJ STERTA TO MINHEAP, czyli najmniejszy na gorze
def sterta(tab, n, i):
    global ilosc_swapow_heap
    global ilosc_porownan_heap
    najmniejszy_element = i
    l = 2 * i + 1  # l - lewy syn
    r = 2 * i + 2  # r - prawy syn

    # by sortowalo w druga strone wystarczy zmienic kierunek 2och nierownosci, to jest jedna z nich...
    ilosc_porownan_heap += 1
    if l < n and tab[i] > tab[l]:
        najmniejszy_element = l
    ilosc_porownan_heap += 1
    if r < n and tab[najmniejszy_element] > tab[r]:  # ...a to druga :P
        najmniejszy_element = r
    ilosc_porownan_heap += 1
    if najmniejszy_element != i:
        ilosc_swapow_heap += 1
        tab[i], tab[najmniejszy_element] = tab[najmniejszy_element], tab[i]
        sterta(tab, n, najmniejszy_element)


def sortowanie_przez_kopcowanie(tab):
    global czas_heap
    global ilosc_swapow_heap
    t0 = time.time()
    n = len(tab)

    # minimalna sterta
    for i in range(n//2, -1, -1):
        sterta(tab, n, i)
    # sciaganie elementow ze sterty
    for i in range(n - 1, 0, -1):
        ilosc_swapow_heap += 1
        tab[i], tab[0] = tab[0], tab[i]
        sterta(tab, i, 0)
    czas_heap = time.time()-t0


#                        ,e,
# 888-~88e-~88e   /~~~8e   "  888-~88e
# 888  888  888       88b 888 888  888
# 888  888  888  e88~-888 888 888  888
# 888  888  888 C888  888 888 888  888
# 888  888  888  "88_-888 888 888  888
# generator list(listy, bo to python)
# losowe
#n = 100000
print('LOSOWE')
for j in range(500, 5000+1, 500):  # powinno byc ich 10
    lista_testowa = []
    for i in range(0, j):
        lista_testowa.append(random.randint(1, 5000))
        twarda_kopia = []
        for e in range(len(lista_testowa)):
            twarda_kopia.append(lista_testowa[e])
    # sortowanie_babelkowe(lista_testowa)
    #print('liczba porownan sortowania babelkowego dla n =', j, ':', ilosc_porownan_bubble)
    #print('liczba swapow sortowania babelkowego dla n =', j, ':', ilosc_swapow_bubble)
    #print('czas sortowania babelkowego dla n =', j, ':', czas_bubble)
    #ilosc_porownan_bubble = 0
    #ilosc_swapow_bubble = 0
    #lista_testowa = twarda_kopia
    # sortowanie_shella(lista_testowa)
    #print('liczba porownan sortowania shella dla n =', j, ':', ilosc_porownan_shell)
    #print('liczba swapow sortowania shella dla n =', j, ':', ilosc_swapow_shell)
    #print('czas sortowania shella dla n =', j, ':', czas_shell)
    #ilosc_porownan_shell = 0
    #ilosc_swapow_shell = 0
    #lista_testowa = twarda_kopia
    #######################################################################################################################
    # sortowanie_przez_wybieranie(lista_testowa)
    #print('liczba porownan sortowania przez wybieranie dla n =', j, ':', ilosc_porownan_selection)
    #ilosc_porownan_selection = 0
    #lista_testowa = twarda_kopia
    #print('czas sortowania kopcowego dla n =', j, ':', czas_selection)
    #######################################################################################################################
    # sortowanie_przez_kopcowanie(lista_testowa)
    #print('liczba porownan sortowania przez kopcowanie dla n =', j, ':', ilosc_porownan_heap)
    #print('liczba swapow sortowania przez kopcowanie dla n =', j, ':', ilosc_swapow_heap)
    #print('czas sortowania przez kopcowanie dla n =', j, ':', czas_heap)
    ilosc_porownan_heap = 0
    ilosc_swapow_heap = 0
    lista_testowa = twarda_kopia
    #sortowanie_szybkie(lista_testowa, 0, len(lista_testowa)-1)
    #print('liczba porownan sortowania szybkiego dla n =', j, ':', ilosc_porownan_quick)
    #print('liczba swapow sortowania szybkiego dla n =', j, ':', ilosc_swapow_quick)
    #print('czas sortowania szybkiego dla n =', j, ':', czas_quick)
    ilosc_porownan_quick = 0
    ilosc_swapow_quick = 0
    lista_testowa = twarda_kopia
    # sortowanie_przez_scalanie(lista_testowa)
    #print('czas sortowania przez scalanie dla n =', j, ':', czas_merge)
    #
    # sortowanie_przez_wstawianie(lista_testowa)
    #print('liczba porownan sortowania przez wstawianie dla n =', j, ':', ilosc_porownan_insertion)
    #print('liczba swapow sortowania przez wstawianie dla n =', j, ':', ilosc_swapow_insertion)
    #print('czas sortowania przez wstawianie dla n =', j, ':', czas_insertion)
    ilosc_porownan_insertion = 0
    ilosc_swapow_insertion = 0
    lista_testowa = twarda_kopia
    # time.sleep(0.1)


print()
print()
print()
print()
print()
print()
print()
print("ROSNACE")
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
for j in range(500, 5000+1, 500):  # powinno byc ich 10
    k = 0
    lista_testowa = []
    for i in range(0, j):
        lista_testowa.append(k)
        k += 1
        twarda_kopia = []
        for e in range(len(lista_testowa)):
            twarda_kopia.append(lista_testowa[e])

    # sortowanie_babelkowe(lista_testowa)
    #print('liczba porownan sortowania babelkowego dla n =', j, ':', ilosc_porownan_bubble)
    #print('liczba swapow sortowania babelkowego dla n =', j, ':', ilosc_swapow_bubble)
    #print('czas sortowania babelkowego dla n =', j, ':', czas_bubble)
    ilosc_porownan_bubble = 0
    ilosc_swapow_bubble = 0
    lista_testowa = twarda_kopia
    # sortowanie_shella(lista_testowa)
    #print('liczba porownan sortowania shella dla n =', j, ':', ilosc_porownan_shell)
    #print('liczba swapow sortowania shella dla n =', j, ':', ilosc_swapow_shell)
    #print('czas sortowania shella dla n =', j, ':', czas_shell)
    ilosc_porownan_shell = 0
    ilosc_swapow_shell = 0
    lista_testowa = twarda_kopia
    #######################################################################################################################
    # sortowanie_przez_wybieranie(lista_testowa)
    #print('liczba porownan sortowania przez wybieranie dla n =', j, ':', ilosc_porownan_selection)
    #print('czas sortowania kopcowego dla n =', j, ':', czas_selection)
    #ilosc_porownan_selection = 0
    #lista_testowa = twarda_kopia
    #######################################################################################################################
    # sortowanie_przez_kopcowanie(lista_testowa)
    #print('liczba porownan sortowania przez kopcowanie dla n =', j, ':', ilosc_porownan_heap)
    #print('liczba swapow sortowania przez kopcowanie dla n =', j, ':', ilosc_swapow_heap)
    #print('czas sortowania kopcowego dla n =', j, ':', czas_heap)
    ilosc_porownan_heap = 0
    ilosc_swapow_heap = 0
    lista_testowa = twarda_kopia
    #sortowanie_szybkie(lista_testowa, 0, len(lista_testowa)-1)
    #print('liczba porownan sortowania szybkiego dla n =', j, ':', ilosc_porownan_quick)
    #print('liczba swapow sortowania szybkiego dla n =', j, ':', ilosc_swapow_quick)
    #print('czas sortowania szybkiego dla n =', j, ':', czas_quick)
    ilosc_porownan_quick = 0
    ilosc_swapow_quick = 0
    lista_testowa = twarda_kopia
    # sortowanie_przez_scalanie(lista_testowa)
    #print('czas sortowania przez scalanie dla n =', j, ':', czas_merge)
    #
    # sortowanie_przez_wstawianie(lista_testowa)
    #print('liczba porownan sortowania przez wstawianie dla n =', j, ':', ilosc_porownan_insertion)
    #print('liczba swapow sortowania przez wstawianie dla n =', j, ':', ilosc_swapow_insertion)
    #print('czas sortowania przez wstawianie dla n =', j, ':', czas_insertion)
    ilosc_porownan_insertion = 0
    ilosc_swapow_insertion = 0
    lista_testowa = twarda_kopia


######################################################################################################################
######################################################################################################################
######################################################################################################################
print()
print()
print()
print()
print()
print()
print()
print("MALEJACE")
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
for j in range(500, 5000+1, 500):  # powinno byc ich 10
    k = 0
    lista_testowa = []
    for i in range(0, j):
        lista_testowa.append(k)
        k -= 1
        twarda_kopia = []
        for e in range(len(lista_testowa)):
            twarda_kopia.append(lista_testowa[e])
    # sortowanie_przez_kopcowanie(lista_testowa)
    #print('liczba swapow sortowania przez kopcowanie dla n =', j, ':', ilosc_swapow_heap)
    # sortowanie_shella(lista_testowa)
    #sortowanie_szybkie(lista_testowa, 0, len(lista_testowa)-1)
    # sortowanie_babelkowe(lista_testowa)
    #print('liczba porownan sortowania babelkowego dla n =', j, ':', ilosc_porownan_bubble)
    #print('liczba swapow sortowania babelkowego dla n =', j, ':', ilosc_swapow_bubble)
    #print('czas sortowania babelkowego dla n =', j, ':', czas_bubble)
    ilosc_porownan_bubble = 0
    ilosc_swapow_bubble = 0
    lista_testowa = twarda_kopia
    # sortowanie_shella(lista_testowa)
    #print('liczba porownan sortowania shella dla n =', j, ':', ilosc_porownan_shell)
    #print('liczba swapow sortowania shella dla n =', j, ':', ilosc_swapow_shell)
    #print('czas sortowania shella dla n =', j, ':', czas_shell)
    ilosc_porownan_shell = 0
    ilosc_swapow_shell = 0
    lista_testowa = twarda_kopia
    #######################################################################################################################
    # sortowanie_przez_wybieranie(lista_testowa)
    #print('liczba porownan sortowania przez wybieranie dla n =', j, ':', ilosc_porownan_selection)
    #ilosc_porownan_selection = 0
    #lista_testowa = twarda_kopia
    #print('czas sortowania kopcowego dla n =', j, ':', czas_selection)
    #######################################################################################################################
    # sortowanie_przez_kopcowanie(lista_testowa)
    #print('liczba porownan sortowania przez kopcowanie dla n =', j, ':', ilosc_porownan_heap)
    #print('liczba swapow sortowania przez kopcowanie dla n =', j, ':', ilosc_swapow_heap)
    #print('czas sortowania przez kopcowanie dla n =', j, ':', czas_heap)
    ilosc_porownan_heap = 0
    ilosc_swapow_heap = 0
    lista_testowa = twarda_kopia
    #sortowanie_szybkie(lista_testowa, 0, len(lista_testowa)-1)
    #print('liczba porownan sortowania szybkiego dla n =', j, ':', ilosc_porownan_quick)
    #print('liczba swapow sortowania szybkiego dla n =', j, ':', ilosc_swapow_quick)
    #print('czas sortowania szybkiego dla n =', j, ':', czas_quick)
    ilosc_porownan_quick = 0
    ilosc_swapow_quick = 0
    lista_testowa = twarda_kopia
    # sortowanie_przez_scalanie(lista_testowa)
    #print('czas sortowania przez scalanie dla n =', j, ':', czas_merge)
    #
    # sortowanie_przez_wstawianie(lista_testowa)
    #print('liczba porownan sortowania przez wstawianie dla n =', j, ':', ilosc_porownan_insertion)
    #print('liczba swapow sortowania przez wstawianie dla n =', j, ':', ilosc_swapow_insertion)
    #print('czas sortowania przez wstawianie dla n =', j, ':', czas_insertion)
    ilosc_porownan_insertion = 0
    ilosc_swapow_insertion = 0
    lista_testowa = twarda_kopia


#######################################################################################################################
#######################################################################################################################
print()
print()
print()
print()
print()
print()
print()
print("A KSZTALTNE")
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
for j in range(500, 5000+1, 500):  # powinno byc ich 10
    k = 0
    lista_testowa = []
    for i in range(0, j):
        lista_testowa.append(k)
        if i < (j/2):
            k += 1
        else:
            k -= 1
        twarda_kopia = []
        for e in range(len(lista_testowa)):
            twarda_kopia.append(lista_testowa[e])

    # sortowanie_babelkowe(lista_testowa)
    #print('liczba porownan sortowania babelkowego dla n =', j, ':', ilosc_porownan_bubble)
    #print('liczba swapow sortowania babelkowego dla n =', j, ':', ilosc_swapow_bubble)
    #print('czas sortowania babelkowego dla n =', j, ':', czas_bubble)
    ilosc_porownan_bubble = 0
    ilosc_swapow_bubble = 0
    lista_testowa = twarda_kopia
    # sortowanie_shella(lista_testowa)
    #print('liczba porownan sortowania shella dla n =', j, ':', ilosc_porownan_shell)
    #print('liczba swapow sortowania shella dla n =', j, ':', ilosc_swapow_shell)
    #print('czas sortowania shella dla n =', j, ':', czas_shell)
    ilosc_porownan_shell = 0
    ilosc_swapow_shell = 0
    lista_testowa = twarda_kopia
    #######################################################################################################################
    # sortowanie_przez_wybieranie(lista_testowa)
    #print('liczba porownan sortowania przez wybieranie dla n =', j, ':', ilosc_porownan_selection)
    #print('czas sortowania kopcowego dla n =', j, ':', czas_selection)
    #ilosc_porownan_selection = 0
    #lista_testowa = twarda_kopia
    #######################################################################################################################
    # sortowanie_przez_kopcowanie(lista_testowa)
    #print('liczba porownan sortowania przez kopcowanie dla n =', j, ':', ilosc_porownan_heap)
    #print('liczba swapow sortowania przez kopcowanie dla n =', j, ':', ilosc_swapow_heap)
    #print('czas sortowania kopcowego dla n =', j, ':', czas_heap)
    ilosc_porownan_heap = 0
    ilosc_swapow_heap = 0
    lista_testowa = twarda_kopia
    #sortowanie_szybkie(lista_testowa, 0, len(lista_testowa)-1)
    #print('liczba porownan sortowania szybkiego dla n =', j, ':', ilosc_porownan_quick)
    #print('liczba swapow sortowania szybkiego dla n =', j, ':', ilosc_swapow_quick)
    #print('czas sortowania szybkiego dla n =', j, ':', czas_quick)
    ilosc_porownan_quick = 0
    ilosc_swapow_quick = 0
    lista_testowa = twarda_kopia
    # sortowanie_przez_scalanie(lista_testowa)
    #print('czas sortowania przez scalanie dla n =', j, ':', czas_merge)
    #
    # sortowanie_przez_wstawianie(lista_testowa)
    #print('liczba porownan sortowania przez wstawianie dla n =', j, ':', ilosc_porownan_insertion)
    #print('liczba swapow sortowania przez wstawianie dla n =', j, ':', ilosc_swapow_insertion)
    #print('czas sortowania przez wstawianie dla n =', j, ':', czas_insertion)
    ilosc_porownan_insertion = 0
    ilosc_swapow_insertion = 0
    lista_testowa = twarda_kopia
######################################################################################################################################
######################################################################################################################################
######################################################################################################################################
print()
print()
print()
print()
print()
print()
print()
print("V KSZTALTNE")
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
for j in range(500, 5000+1, 500):  # powinno byc ich 10
    k = 0
    lista_testowa = []
    for i in range(0, j):
        lista_testowa.append(k)
        if i < (j/2):
            k -= 1
        else:
            k += 1
        twarda_kopia = []
        for e in range(len(lista_testowa)):
            twarda_kopia.append(lista_testowa[e])

    # sortowanie_babelkowe(lista_testowa)
    #print('liczba porownan sortowania babelkowego dla n =', j, ':', ilosc_porownan_bubble)
    #print('liczba swapow sortowania babelkowego dla n =', j, ':', ilosc_swapow_bubble)
    #print('czas sortowania babelkowego dla n =', j, ':', czas_bubble)
    ilosc_porownan_bubble = 0
    ilosc_swapow_bubble = 0
    lista_testowa = twarda_kopia
    # sortowanie_shella(lista_testowa)
    #print('liczba porownan sortowania shella dla n =', j, ':', ilosc_porownan_shell)
    #print('liczba swapow sortowania shella dla n =', j, ':', ilosc_swapow_shell)
    #print('czas sortowania shella dla n =', j, ':', czas_shell)
    ilosc_porownan_shell = 0
    ilosc_swapow_shell = 0
    lista_testowa = twarda_kopia
    #######################################################################################################################
    # sortowanie_przez_wybieranie(lista_testowa)
    #print('liczba porownan sortowania przez wybieranie dla n =', j, ':', ilosc_porownan_selection)
    #ilosc_porownan_selection = 0
    #lista_testowa = twarda_kopia
    #print('czas sortowania przez wybieranie dla n =', j, ':', czas_selection)
    #######################################################################################################################
    # sortowanie_przez_kopcowanie(lista_testowa)
    #print('liczba porownan sortowania przez kopcowanie dla n =', j, ':', ilosc_porownan_heap)
    #print('liczba swapow sortowania przez kopcowanie dla n =', j, ':', ilosc_swapow_heap)
    #print('czas sortowania kopcowego dla n =', j, ':', czas_heap)
    ilosc_porownan_heap = 0
    ilosc_swapow_heap = 0
    lista_testowa = twarda_kopia
    #sortowanie_szybkie(lista_testowa, 0, len(lista_testowa)-1)
    #print('liczba porownan sortowania szybkiego dla n =', j, ':', ilosc_porownan_quick)
    #print('liczba swapow sortowania szybkiego dla n =', j, ':', ilosc_swapow_quick)
    #print('czas sortowania szybkiego dla n =', j, ':', czas_quick)
    ilosc_porownan_quick = 0
    ilosc_swapow_quick = 0
    lista_testowa = twarda_kopia
    # sortowanie_przez_scalanie(lista_testowa)
    #print('czas sortowania przez scalanie dla n =', j, ':', czas_merge)
    #
    # sortowanie_przez_wstawianie(lista_testowa)
    #print('liczba porownan sortowania przez wstawianie dla n =', j, ':', ilosc_porownan_insertion)
    #print('liczba swapow sortowania przez wstawianie dla n =', j, ':', ilosc_swapow_insertion)
    #print('czas sortowania przez wstawianie dla n =', j, ':', czas_insertion)
    ilosc_porownan_insertion = 0
    ilosc_swapow_insertion = 0
    lista_testowa = twarda_kopia


input()
