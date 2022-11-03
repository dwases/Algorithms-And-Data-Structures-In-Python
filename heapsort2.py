
# TUTAJ STERTA TO MINHEAP, czyli najmniejszy na gorze
def sterta(tab, n, i):
    najmniejszy_element = i
    l = 2 * i + 1  # l - lewy syn
    r = 2 * i + 2  # r - prawy syn

    # by sortowalo w druga strone wystarczy zmienic kierunek 2och nierownosci, to jest jedna z nich...
    if l < n and tab[i] > tab[l]:
        najmniejszy_element = l
    if r < n and tab[najmniejszy_element] > tab[r]:  # ...a to druga :P
        najmniejszy_element = r
    if najmniejszy_element != i:
        tab[i], tab[najmniejszy_element] = tab[najmniejszy_element], tab[i]
        sterta(tab, n, najmniejszy_element)


def heapSort(tab):
    n = len(tab)

    # minimalna sterta
    for i in range(n//2, -1, -1):
        sterta(tab, n, i)
    # sciaganie elementow
    for i in range(n - 1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        sterta(tab, i, 0)


# Driver code
tab = [11, 34, 9, 5, 16, 10]
n = len(tab)
print("Original array:")
for i in range(n):
    print("%d " % tab[i], end='')
heapSort(tab)
print("Sorted array:")
for i in range(n):
    print("%d " % tab[i], end='')
