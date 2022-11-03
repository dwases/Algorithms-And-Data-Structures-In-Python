import copy
import random
import time
# nierosnace

# konwertuje stringa na liste wedlug znakow


def split(word):
    return [char for char in word]

# bubble sort wedlug worthness


def sortowanie(tab):
    n = len(tab)
    while n > 1:
        for i in range(n-1):
            # jak sie zmieni znak rownosci na druga strone to bedzie sortowanie w druga strone :P
            if tab[i].worthness < tab[i+1].worthness:
                tab[i], tab[i+1] = tab[i+1], tab[i]
        n -= 1

    return tab


class Item:
    def __init__(self, weight, price):
        self.weight = weight
        self.price = price
        self.worthness = price/weight

    # poprawic potem - jednak nie, w sumie to chyba nie ma sensu
    def __str__(self):
        return self.price

# silowy
# dziala


def brute_force(items, c):
    x = []  # liczba binarna
    rozw = []  # lista dopuszczalnych rozwiazan
    knapsack = []
    #fs = []
    fmax = 0
    xbest = None
    for i in range(1, 2**len(items)):
        w = 0
        f = 0
        pointer = 0
        x = list(reversed(split(bin(i)[2:])))
        for j in range(len(x)):
            if x[j] == '1':
                w += int(items[j].weight)
                f += int(items[j].price)
#            if w <= c:
#                rozw.append(x)
                if f > fmax:
                    xbest = fmax
    # print(max(fs))

# to juz dziala

# zachalnny


def greedy(items, c):
    itemscopy = copy.deepcopy(items)
    knapsack = []
    i = 0
    w = 0  # waga plecaka
    while(w+items[i].weight <= c):
        w += items[i].weight
        knapsack.append(items[i])
        i += 1
        if i >= len(items):
            break
    # for el in knapsack:
        #print(el.weight, el.price, el.worthness)


def dynamiczny(items, c):
    macierzPD = [[0 for i in range(c+1)] for j in range(len(items)+1)]
    # wypelnienie macierzy zerami
    # for el in macierzPD:   #dziala
    #    print(el)
    for i in range(len(items)+1):
        for j in range(c+1):
            macierzPD[i][j] = 0
    for i in range(1, len(items)+1):
        for j in range(1, c+1):
            if items[i-1].weight > j:
                macierzPD[i][j] = macierzPD[i-1][j]
            if items[i-1].weight <= j:
                macierzPD[i][j] = max([macierzPD[i-1][j], macierzPD[i-1]
                                      [j-items[i-1].weight]+items[i-1].price])
    # for el in macierzPD:
    #    print(el)
    f = max(max(x) for x in macierzPD)
    #print("f =", f)
    x = len(macierzPD[0])
    y = len(macierzPD)
    for i in range(len(macierzPD)+1, 0, -1):
        pass


# c = 8
# items = []
# items.append(Item(2, 4))
# items.append(Item(1, 3))
# items.append(Item(4, 6))
# items.append(Item(4, 8))
# print(sortowanie([1, 5, 2, 56, 1, 27, 2, -927]))

# sortowanie(items)  # to zadzialalo
# items.brute_force(items)
# for i in items:
#    print(i.worthness)
# items.greedy(items, c)
# sortowanie(items)
# print("wynik zachlannego")
# greedy(items, c)  # dziala
# print(bin(4)[2:])  # to jest string jakby co
# print(split(bin(5)[2:]))
# print("wynik silowego")
# brute_force(items, c)
# x = list(reversed(split(bin(6)[2:])))  # dziala
# print(x)
# print("wynik dynamicznego")
# dynamiczny(items, c)
#print("t    afkb")
# wykres 1
for c in range(100, 1100, 100):
    items = []
    for i in range(22):
        items.append(Item(random.randrange(1, 20), random.randrange(1, 20)))
    #print("wynik zachlannego")
    t0 = time.time()
    sortowanie(items)
    greedy(items, c)
    t1 = time.time() - t0
    #print("wynik dynamicznego")
    t0 = time.time()
    dynamiczny(items, c)
    t1 = time.time() - t0
    # print(t1)
    #print("wynik silowego")
    t0 = time.time()
    brute_force(items, c)
    t1 = time.time() - t0
    print(t1)
