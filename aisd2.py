"""
"""
# wymaga 'pip install binarytree' wpisanego w terminal
import random   # dobra to tez sie nie przyda jednak
import time
import sys
import binarytree  # na potrzeby wypisania drzewa
import sys
flag = False  # to jest global na potrzeby preorder dla pozadanego klucza
root = None  # jednak sie nie przydalo, zreszta i tak bylby to fatalny pomysl


class WierzcholekBST(object):
    # atrybuty wierzcholka
    def __init__(self, klucz=None):  # klucz domyslnie wartosc None
        self.right = None  # prawy syn - tez bedzie wierzcholkiem
        self.left = None  # lewy syn - tez bedzie wierzcholkiem
        self.klucz = klucz  # wartosc klucza

    # zrodlo - https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    # zrodlo - https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.klucz
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.klucz
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.klucz
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.klucz
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def wprowadz_wierzcholek(self, klucz):  # umieszcza nowy wierzcholek w BST
        if not self.klucz:  # jesli nie ma zadnych kluczy, czyli nie ma jeszcze
            self.klucz = klucz
            return

        if self.klucz == klucz:  # warunek gdy wartosci sie powtarzaja, ale nie wiem czy go zostawic
            return

        if klucz < self.klucz:  # jesli nowy klucz jest mniejszy od klucza wierzcholka na ktorym jest algorytm
            if self.left:  # jesli lewy syn istnieje
                # wstawia nowy wierzcholek o kluczu wprowadzanym do drzewa w lewa strone rekurencyjnie
                self.left.wprowadz_wierzcholek(klucz)
                return
            # jesli lewy syn nie istnieje to ten nowy klucz sie nim staje
            self.left = WierzcholekBST(klucz)
            return

        if self.right:  # jesli prawy syn istnieje
            # rekurencyjnie wrzuca klucz o nowej wartosci na prawo
            self.right.wprowadz_wierzcholek(klucz)
            return
        self.right = WierzcholekBST(klucz)  # nowy klucz staje sie prawym synem

    def minimum(self):  # zwraca najmniejszy klucz
        wskaznik = self  # wskaznik to tutaj caly wierzcholek na ktorym jestesmy
        print(wskaznik.klucz)
        # dobra, ten sposob jednak nie dziala :( - a teraz jeszcze indentacja jest zepsuta - jakis zart
        # while(True):  # return to warunek stopu dla tej petli
        #    if wskaznik.left == None:  # jesli nie ma lewego syna
        #        return self.klucz  # zwraca najmniejsza wartosc - NIE wierzcholek sam w sobie
        #    else:
        # to po to zeby wypisac na ekran wartosci przez ktore przechodzimy
        #        print(wskaznik.klucz)
        #        wskaznik = wskaznik.left  # przesuwam wskaznik na lewego syna
        ####
        while wskaznik.left:
            wskaznik = wskaznik.left
            print(wskaznik.klucz)
        return wskaznik.klucz

        # to dziala analogicznie do min na gorze, to chyba poradze sobie bez komentarza jak wroce jutro
    def maksimum(self):
        wskaznik = self  # wskaznik to tutaj caly wierzcholek na ktorym jestesmy
        print(wskaznik.klucz)
        while wskaznik.right:
            wskaznik = wskaznik.right
            print(wskaznik.klucz)
        return wskaznik.klucz

    # inorder - ok, juz jest dobrze
    def inorder(self, tablica):
        if self.left:
            self.left.inorder(tablica)
        if self.klucz:
            tablica.append(self.klucz)
        if self.right:
            self.right.inorder(tablica)
        return tablica

        # na razie nie wiem ktory preorder jest lepszy to zostawie ten pierwszy
        # wypisanie preorder calego drzewa

    def preorder(self, tablica):  # potrzebuje pustej tablicy jako argument - wpisuje klucze wlasnie do niej
        # print(self.klucz)        #to bylo na potrzeby testowe, ale juz dziala - teraz pierwszym elementem na pewno jest korzen a nie None
        if self.klucz:
            tablica.append(self.klucz)  # nie dopisuje tylko jak wierzcholek jest None
        if self.left:  # jesli istnieje lewy syn
            self.left.preorder(tablica)  # rekurencja - dorzuca lewego syna do tablicy
        if self.right:  # jesli istnieje prawy syn
            self.right.preorder(tablica)  # rekurencja - dorzuca prawego syna do tablicy
        return tablica  # zwraca wynik preorder w postaci tablicy

      # wypisanie postorder calego drzewa i usuniecie go zarazem
      # jak preorder, ale kolejnosc zmieniona, bo wowczas mamy najpierw nizsze kondygnacje drzewa az dojdziemy do korzenia

    def postorder(self, tablica):
        if self.left:
            self.left.postorder(tablica)
        if self.right:
            self.right.postorder(tablica)
        if self.klucz:
            tablica.append(self.klucz)
            # usuwanie odbywa sie tutaj
            self.left = None
            self.right = None
            self.klucz = None
        return tablica

        # tutaj jest preorder dla poddrzewa o wartosci klucza wprowadzonej systemowo
        # faza wczesnej alfy nawiasem mowiac, - dobra juz nie, ale tbh to nie wiem czy dobrze dziala - musze zrobic wiecej testow, ale chociaz juz nie wyrzuca bledow na kazdym kroku
    def key_preorder(self, tablica, wartosc):
        global flag

        if self.klucz == wartosc:
            flag = True
        if flag == True:  # tak naprawde jedyna roznica - powinno wypisywac wartosci tylko key i potomkow key
            # nie dopisuje tylko jak wierzcholek jest None, warunek brzegowy
            tablica.append(self.klucz)
        if self.left:  # jesli istnieje lewy syn
            self.left.key_preorder(tablica, wartosc)  # rekurencja - dorzuca lewego syna do tablicy
        if self.right:  # jesli istnieje prawy syn
            # rekurencja - dorzuca prawego syna do tablicy
            self.right.key_preorder(tablica, wartosc)
        return tablica  # zwraca wynik preorder w postaci tablicy

    def usun_wierzcholek(self, klucz):
        # warunek graniczny
        if self.klucz == None:
            return self
        # szukanie klucza
        if klucz < self.klucz:
            self.left = self.left.usun_wierzcholek(klucz)
            return self
        if klucz > self.klucz:
            self.right = self.right.usun_wierzcholek(klucz)
            return self
        # dla 0 potomkow
        if (self.left == None) and (self.right == None):
            return self
        # dla jednego dziecka
        if self.right == None and (self.left != None):
            wskaznik = self.left
            self = None
            return wskaznik  # w wskazniku przechowuje usuniety wierzcholek
        elif self.left == None and (self.right != None):
            wskaznik = self.right
            self = None
            return wskaznik  # w wskazniku przechowuje usuniety wierzcholek
        # dla 2 potomkow
        wskaznik3 = self.right
        wskaznik2 = self
        while wskaznik3.left:
            wskaznik2 = wskaznik3
            wskaznik3 = wskaznik3.left
        if wskaznik2 != self:
            wskaznik2.left = wskaznik3.right
        else:
            wskaznik2.right = wskaznik3.right
        self.klucz = wskaznik3.klucz
        return self

    # na portrzeby rownowazenia drzewa
    # to tez nie??? czm?
    def height(self):  # w pewnym momencie nagle przestalo dzialac i nwm czemu
        if self is None:
            return self
        return 1 + max(self.left.height(), self.right.height())

    # to tez do rownowazenia - troche niepotrzebne, ale chociaz abstrakcja wzrasta- chyba
    def wspolczynnik_rownowagi(self):
        return self.left.height() - self.right.height()

    # bfs do balansowania
    # dobra to juz dziala
    # testowo zeby sprawdzic czy dziala
    def bfs(self):
        tablica = []
        tablica.append(self)
        klucze = []
        while tablica:
            self = tablica.pop(0)
            klucze.append(self.klucz)
            if(self.left):
                tablica.append(self.left)
            if(self.right):
                tablica.append(self.right)
        return tablica  # mozna zmieniac miedzy klucze i tablica

        # dalej rownowazenie ni dziala
        # probowalem tez przez dsw ale glownie usuwanie korzenia
        # chociaz height juz dzialalo to znowu jest niefunkcjonalne
        # wspolczynnik rownowagi jest poprawny abstrachujac od height
        # bfs dziala dobrze
        # usuwanie wezlow tez
        # brakuje tylko height...
    def rownowazenie(self):
        for i in range(self.bfs()):
            if abs(self.bfs()[i].wspolczynnik_rownowagi) > 1:
                ws
                self.wprowadz_wierzcholek(self.bfs()[i].klucz)
        else:
            return

    # buduje drzewo AVL na podstawie listy - wymaga posortowanych danych
    def buduj_AVL(self, tablica):
        mediana = tablica[len(tablica)//2]
        self.wprowadz_wierzcholek(mediana)
        if mediana != tablica[0]:
            tab1 = tablica[:len(tablica)//2]
        else:
            tab1 = []
        if mediana != tablica[-1]:
            tab2 = tablica[(len(tablica)+1)//2:]
        else:
            tab2 = []

        if tab1:
            self.buduj_AVL(tab1)
        if tab2:
            self.buduj_AVL(tab2)

    # zamienia drzewo BST w AVL dzieki czemu wszystkie metody dla BST staja sie uniwersalne
    def transformuj_na_AVL(self):
        tablica = self.inorder([])
        self.postorder([])
        self.buduj_AVL(tablica)

    # nieuniwersalne
    # wymaga winorosli na odwrot
    # EDIT: nie uzywac - koniec koncow jedynie wyrzuca roota na sam dol
    def transformuj_na_winorosl(self):
        if self.left == None:
            return
        else:
            tmp = self.klucz
            self.klucz = self.left.klucz
            self.left.klucz = tmp
            if self.left.klucz != None:
                self.left.transformuj_na_winorosl()


#
#    def bfs(self):
#        kolejka = [self]
#        if self.left:
#            kolejka.append(self.left)
#        if self.right:
#            kolejka.append(self.right)
#        print(kolejka.pop(0))

#    def traverse(rootnode):
#        thislevel = [rootnode]
#        while thislevel:
#            nextlevel = list()
#        for n in thislevel:
#            print n.value,
#            if n.left:
#                nextlevel.append(n.left)
# nextlevel.append(n.right)
#        print
#        thislevel = nextlevel

    # breadth first search na potrzeby balansowania
    # def bfs(self):
    #    queue = [self]
    #    while queue != []:
    #        popped = queue.pop(0)
    #        for child in popped.children:
    #            queue.append(child)
    #        print(popped.key, end=' ')

##################################################################
# za bfs odpowiadaja 2 funkcje, bo inaczej sa problemy z rekursja
#    def bfs(self):
#        for i in range(1, self.wysokosc()+1):
#            bfs2()

#    def
##################################################################
#    def create_vine(self):
#        #global root
#        tmp = self
#        while(tmp != None):
#            if(tmp.left.klucz != None):
        # right rotate left child aroung tmp
#                pass
#            else:
#                tmp = tmp.prawy


"""
1. Przechodząc po drzewie od korzenia w kierunku liści metodą BFS
(poziomami), znajdź pierwszy węzeł wi
, dla którego |bfi
|>1, gdzie bfi
to
współczynnik równowagi węzła wi
. Jeśli nie ma takiego węzła to zakończ
(drzewo jest zrównoważone). W przeciwnym razie idź do pkt 2.
2. Usuń węzeł wi
z drzewa (jeśli wi ma dwa poddrzewa, to zastąp wi węzłem
z poddrzewa o większej wysokości). Następnie wstaw klucz ki
z powrotem
do drzewa (ki
to klucz usuniętego węzła wi
).
3. Zaktualizuj współczynniki równowagi w całym drzewie. Wróć do pkt 1.
"""


# to jest drugi sposob na preorder, ale jeszcze nie testowalem tego
"""
        def preorder(self):
            if self.klucz:
                print(self.klucz)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
"""


# rownowazenie drzewa za pomoca dsw - to beda dwie funkcje
"""z wikipedii pseudokod
   TworzKregoslup (węzeł korzen)
       tmp = korzen; //tmp to zmienna tymczasowa
       while tmp nie jest równe NULL
           if tmp posiada lewego potomka
               wykonaj rotację tego potomka względem tmp; //Czyli lewy potomek zostaje ojcem węzła tmp
               tmp zostaje przesunięty do nowo powstałego rodzica;
           else
               tmp zostaje przesunięty w miejsce swojego prawego potomka;
"""
#    def tworz_kregoslup(self):
#        tmp = self
#        while tmp:
#            if tmp.left:
# dobra - juz lepiej zrobie przez usuwanie korzenia


# tab = [4, 8, 9, 6, 5, 7, 2, 1, 3]  # klucze, ktore beda wrzucane do drzewa
# for el in tab:
#    wprowadz_wierzcholek(el)
# drzewoBST = WierzcholekBST()  # utworzenie instancji drzewa BST
# for el in tab:
#    drzewoBST.wprowadz_wierzcholek(el)
# print(drzewoBST)
# drzewoBST.display()  # dziala
# drzewoBST.transformuj_na_AVL()
# drzewoBST.bfs()
# print(drzewoBST.bfs())
#print("wysokosc ", drzewoBST.wysokosc())
#print("minimum: ", drzewoBST.minimum())
#print("maksimum: ", drzewoBST.maksimum())
# drzewoBST.usun_wierzcholek(8)
# drzewoBST.display()
# drzewoBST.usun_wierzcholek(4)
# drzewoBST.display()
# print("inorder: ", drzewoBST.inorder([]))  # teraz dziala
# print("preorder: ", drzewoBST.preorder([]))  # dobra, to już dziala na stowe
#print("preorder dla key = 6: ", drzewoBST.key_preorder([], 6))
# to najlepiej sprawdzac na samym koncu, bo USUWA CALE DRZEWO
# drzewoBST.usun_wierzcholek(9)      #to jeszcze nie dziala i nie wiem czemu
#print("postorder: ", drzewoBST.postorder([]))
# o - usuwanie w postorder dziala :O EDIT: sam postorder w koncu tez
#print("preorder: ", drzewoBST.preorder([]))
#drzewoAVL = WierzcholekBST()
# drzewoAVL.buduj_AVL(tab)
# drzewoAVL.display()
sys.setrecursionlimit(2000)
###poligon testowy###
# testowanie czasu tworzenia dla bst
#k = []
# for i in range(1000, 0, -1):
#    k.append(i)
# print(k)
#drzewoBST = WierzcholekBST()

#start = time.time()
# for el in k:
#    drzewoBST.wprowadz_wierzcholek(el)
#end = time.time()
#czas = end - start
# print(czas)
#drzewoBST = WierzcholekBST()
# testowanie czasu tworzenia dla avl
#k = []
# for i in range(100, 0, -1):
#    k.append(i)
#drzewoAVL = WierzcholekBST()
# drzewoAVL.buduj_AVL(k)
# drzewoAVL.display()
#drzewoAVL = WierzcholekBST()

# drzewoAVL.buduj_AVL(k)

#czas = end - start
# print(czas)
# drzewoAVL.display()
#start = time.time()
# for el in k:
#    drzewoBST.wprowadz_wierzcholek(el)
#start = time.time()
# drzewoBST.minimum()
#end = time.time()
#czas = end - start
#print("minimum bst- czas: ", czas)
#wypisanie in-order
#k = []
# for i in range(20, 0, -1):
#    k.append(i)

#drzewoBST = WierzcholekBST()
# for el in k:
#    drzewoBST.wprowadz_wierzcholek(el)

#start = time.time()
# drzewoAVL.inorder([])
#end = time.time()
#czas = end - start
# print(czas)
# drzewoBST.display()
# drzewoBST.transformuj_na_winorosl()
# drzewoBST.display()
# print(drzewoBST.height())
# print(drzewoBST.wysokosc())
drzewo = WierzcholekBST()
while True:
    print("Wybierz opcje:")
    print("0 - opusc program")
    print("1 - wyszukaj minimum")
    print("2 - wyszukaj maksimum")
    print("3 - wypisz inorder")
    print("4 - wypisz preorder")
    print("5 - wypisz postorder i usun drzewo")
    # print("rownowazenie placeholder")   #height dalej nie dziala tyloma sposobami, nie czaje kompletnie
    print("6 - zbuduj avl")
    print("7 - skonwertuj na avl")
    print("8 - zbuduj bst")
    print("9 - wyswietl drzewo")
    choice = int(input())
    if choice == 0:
        sys.exit(0)
    elif choice == 1:
        print(drzewo.minimum())
    elif choice == 2:
        print(drzewo.maksimum())
    elif choice == 3:
        print(drzewo.inorder([]))
    elif choice == 4:
        print(drzewo.preorder([]))
    elif choice == 5:
        print(drzewo.postorder([]))
    elif choice == 6:
        tablica = input().split()
        for i in range(len(tablica)):
            tablica[i] = int(tablica[i])
        tablica.sort()
        drzewo.buduj_AVL(tablica)
    elif choice == 7:
        drzewo.transformuj_na_AVL()
    elif choice == 8:
        tablica = input().split()
        for i in range(len(tablica)):
            tablica[i] = int(tablica[i])
        for el in tablica:
            drzewo.wprowadz_wierzcholek(el)
    elif choice == 9:
        drzewo.display()
    else:
        print("niezrozumiale polecenie")

c = input()
