import binarytree  # na potrzeby wypisania drzewa


class WierzcholekAVL(object):
    def __init__(self, klucz=None):
        self.klucz = klucz
        self.left = None
        self.right = None

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
            self.left = WierzcholekAVL(klucz)
            return

        if self.right:  # jesli prawy syn istnieje
            # rekurencyjnie wrzuca klucz o nowej wartosci na prawo
            self.right.wprowadz_wierzcholek(klucz)
            return
        self.right = WierzcholekAVL(klucz)  # nowy klucz staje sie prawym synem

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


tab = [8, 2, 5, 14, 10, 12, 13, 6, 9]
tab.sort()
print(tab)
drzewoAVL = WierzcholekAVL()
# for el in tab:
#    drzewoAVL.wprowadz_wierzcholek(el)
drzewoAVL.buduj_AVL(tab)
drzewoAVL.display()
